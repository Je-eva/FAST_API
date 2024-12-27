from fastapi import FastAPI , HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
import models
from database import engine, SessionLocal

# Initialize the FastAPI application
app = FastAPI()

# Create database tables based on models if they do not already exist
models.Base.metadata.create_all(bind=engine)

# Dependency for handling database sessions
# This function provides a database session and ensures it is properly closed after use
def get_db():
    try:
        db = SessionLocal()  # Create a new database session
        yield db  # Provide the session to the request handler
    finally:
        db.close()  # Close the session to free up resources

# Define the schema for the Book model using Pydantic for validation
class Book(BaseModel):
    title: str = Field(min_length=1)  # Title must be at least 1 character long
    author: str = Field(min_length=2, max_length=60)  # Author name must be 2-60 characters long
    desc: str = Field(min_length=5, max_length=100)  # Description must be 5-100 characters long
    rating: int = Field(gt=-1, lt=101)  # Rating must be between 0 and 100

# Initialize a placeholder list for in-memory books (not used with SQLAlchemy)
books = []

# Route to fetch all books from the database
@app.get("/")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.Books).all()  # Query and return all books from the database

# Route to add a new book to the database
@app.post("/")
def create_book(book: Book, db: Session = Depends(get_db)):
    # Create a new instance of the Books model
    book_model = models.Books()
    book_model.title = book.title
    book_model.author = book.author
    book_model.desc = book.desc
    book_model.rating = book.rating

    # Add the new book to the database
    db.add(book_model)
    db.commit()  # Save the changes to the database

    return book  # Return the book data as a response

# Route to update an existing book in the database
@app.put("/{book_id}")
def update_book(book_id: int, book: Book, db: Session = Depends(get_db)):
    # Find the book in the database by its ID
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()

    # If the book does not exist, raise an error
    if book_model is None:
        raise HTTPException(status_code=404, detail=f"ID {book_id} doesn't exist")

    # Update the book fields with new values
    book_model.title = book.title
    book_model.author = book.author
    book_model.desc = book.desc
    book_model.rating = book.rating

    # Commit the changes to save the updates
    db.commit()

    return book  # Return the updated book data

# Route to delete a book from the database by its ID
@app.delete("/{id}")
def delete_book(id: int, db: Session = Depends(get_db)):
    # Find the book in the database by its ID
    book_model = db.query(models.Books).filter(models.Books.id == id).first()

    # If the book does not exist, raise an error
    if book_model is None:
        raise HTTPException(status_code=404, detail=f"ID {id} doesn't exist")

    # Delete the book from the database
    db.query(models.Books).filter(models.Books.id == id).delete()
    db.commit()  # Save the changes to the database

    return {"detail": f"Book with ID {id} has been deleted"}  # Return confirmation
