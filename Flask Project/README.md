# Flask Assignment Viewer

A web application to view and manage programming assignments organized by category.

## Features

- User registration with Full Name, Email, and Password
- User login with Email and Password
- Personalized welcome message showing first name
- View assignments organized by:
  - Book Assignments (organized by chapters)
  - Web Scraping
  - Section Assignments
- View code and output files for each assignment

## Installation

1. Install Python 3.7 or higher
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Navigate to the Flask Project directory:
```bash
cd "Flask Project"
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```



## Project Structure

```
Flask Project/
├── app.py                 # Main Flask application
├── database.db            # SQLite database (created automatically)
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── static/
│   └── style.css         # CSS styles
└── templates/
    ├── login.html        # Login page
    ├── signup.html       # Registration page
    ├── home.html         # Home page with assignments
    ├── view_code.html    # Code viewer template
    └── view_csv.html     # CSV viewer template
```

## Database

The application uses SQLite database with the following schema:
- `users` table: id, full_name, email, password

The database is automatically created on first run.

## Security Notes

- Passwords are stored in plain text (for development only)
- For production, implement password hashing (e.g., using bcrypt)
- Use HTTPS in production
- Implement proper session management
- Add rate limiting for login attempts

