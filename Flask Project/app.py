from flask import Flask, render_template, request, redirect, session
import sqlite3
import os
from pathlib import Path

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'  # Change this in production!

# Get the base directory (parent of Flask Project)
BASE_DIR = Path(__file__).parent.parent

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # Check if table exists and what columns it has
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    table_exists = c.fetchone()
    
    if table_exists:
        # Check if old schema exists (has username column but no email)
        c.execute("PRAGMA table_info(users)")
        columns = [column[1] for column in c.fetchall()]
        
        if 'username' in columns and 'email' not in columns:
            # Old schema detected - drop and recreate with new schema
            # Note: This will delete existing users. For production, implement proper migration.
            c.execute('DROP TABLE users')
            c.execute('''CREATE TABLE users 
                        (id INTEGER PRIMARY KEY, full_name TEXT, email TEXT, password TEXT)''')
            conn.commit()
        elif 'email' not in columns:
            # Table exists but missing email column - recreate
            c.execute('DROP TABLE users')
            c.execute('''CREATE TABLE users 
                        (id INTEGER PRIMARY KEY, full_name TEXT, email TEXT, password TEXT)''')
            conn.commit()
    else:
        # Create new table with correct schema
        c.execute('''CREATE TABLE users 
                    (id INTEGER PRIMARY KEY, full_name TEXT, email TEXT, password TEXT)''')
        conn.commit()
    
    conn.close()

def get_first_name(full_name):
    """Extract first name from full name"""
    if full_name:
        return full_name.split()[0] if full_name.split() else full_name
    return "User"

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/home')
    return redirect('/signup')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']
        
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        # Check if email already exists
        c.execute('SELECT * FROM users WHERE email=?', (email,))
        if c.fetchone():
            conn.close()
            return render_template('signup.html', error='Email already registered')
        
        c.execute('INSERT INTO users (full_name, email, password) VALUES (?, ?, ?)', 
                (full_name, email, password))
        conn.commit()
        conn.close()
        
        return redirect('/login')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE email=? AND password=?', (email, password))
        user = c.fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user[0]
            session['full_name'] = user[1]
            session['email'] = user[2]
            return redirect('/home')
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect('/login')
    
    first_name = get_first_name(session.get('full_name', ''))
    
    # Get assignment directories
    book_assignments_path = BASE_DIR / 'Book-Assignments'
    web_scraping_path = BASE_DIR / 'Web Scraping'
    sections_assignments_path = BASE_DIR / 'Sections-Assignments'
    
    # Get chapters for Book Assignments
    book_chapters = []
    if book_assignments_path.exists():
        # Get all chapter directories
        chapter_dirs = []
        for item in book_assignments_path.iterdir():
            if item.is_dir() and item.name.startswith('Chapter'):
                # Extract chapter number for sorting
                try:
                    chapter_num = int(item.name.split()[1])
                    files = [f.name for f in item.iterdir() if f.suffix == '.py']
                    chapter_dirs.append((chapter_num, item.name, sorted(files)))
                except (IndexError, ValueError):
                    # If chapter number can't be extracted, add at end
                    files = [f.name for f in item.iterdir() if f.suffix == '.py']
                    chapter_dirs.append((999, item.name, sorted(files)))
        
        # Sort by chapter number and create list
        chapter_dirs.sort(key=lambda x: x[0])
        book_chapters = [{'name': name, 'files': files} for _, name, files in chapter_dirs]
    
    # Get files for Web Scraping
    web_scraping_files = []
    if web_scraping_path.exists():
        web_scraping_files = [f.name for f in web_scraping_path.iterdir() 
                            if f.suffix == '.py' or f.suffix == '.csv']
    
    # Get files for Sections Assignments
    sections_files = []
    if sections_assignments_path.exists():
        sections_files = [f.name for f in sections_assignments_path.iterdir() 
                        if f.suffix == '.py']
    
    return render_template('home.html', 
                        first_name=first_name,
                        book_chapters=book_chapters,
                        web_scraping_files=web_scraping_files,
                        sections_files=sections_files)

@app.route('/view/book/<chapter>/<filename>')
def view_book_assignment(chapter, filename):
    if 'user_id' not in session:
        return redirect('/login')
    
    file_path = BASE_DIR / 'Book-Assignments' / chapter / filename
    if not file_path.exists() or file_path.suffix != '.py':
        return "File not found", 404
    
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()
    
    return render_template('view_code.html', 
                        code=code, 
                        title=f"{chapter} - {filename}",
                        assignment_type="Book Assignment")

@app.route('/view/web-scraping/<filename>')
def view_web_scraping(filename):
    if 'user_id' not in session:
        return redirect('/login')
    
    file_path = BASE_DIR / 'Web Scraping' / filename
    
    if not file_path.exists():
        return "File not found", 404
    
    if file_path.suffix == '.py':
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        return render_template('view_code.html', 
                            code=code, 
                            title=f"Web Scraping - {filename}",
                            assignment_type="Web Scraping")
    elif file_path.suffix == '.csv':
        with open(file_path, 'r', encoding='utf-8') as f:
            csv_data = f.read()
        return render_template('view_csv.html', 
                            csv_data=csv_data, 
                            title=f"Web Scraping - {filename}",
                            assignment_type="Web Scraping")
    else:
        return "Unsupported file type", 400

@app.route('/view/sections/<filename>')
def view_sections_assignment(filename):
    if 'user_id' not in session:
        return redirect('/login')
    
    file_path = BASE_DIR / 'Sections-Assignments' / filename
    if not file_path.exists() or file_path.suffix != '.py':
        return "File not found", 404
    
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()
    
    return render_template('view_code.html', 
                        code=code, 
                        title=f"Section Assignment - {filename}",
                        assignment_type="Section Assignment")

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)