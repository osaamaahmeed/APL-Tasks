from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine('sqlite:///:memory:', echo=False)

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}')"


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


book1 = Book(title='Python Basics', author='Guido')
book2 = Book(title='AI with Python', author='Mohamed')

session.add(book1)
session.add(book2)
session.commit()

all_books = session.query(Book).all()

for book in all_books:
    print(book)