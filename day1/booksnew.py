from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import List

app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=2, max_length=60)
    desc: str = Field(min_length=5, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

class Config:
        json_schema_extra = {
            "example": {
                "title": "A New Dawn",
                "author": "Je-eva",
                "description": "An intriguing story about resilience.",
                "rating": 5,
                "published_date": 2025,
            }
        }


# Initialize an empty list to store books
books: List[Book] = []

@app.get("/", status_code=200)
def read_all_books():
    return books

@app.get("/books/{book_id}", status_code=200)
def read_book(book_id: UUID):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books/byauthor/", status_code=200)
def read_books_by_author(author: str):
    books_to_return = [book for book in books if book.author.casefold() == author.casefold()]
    if not books_to_return:
        raise HTTPException(status_code=404, detail="No books found for this author")
    return books_to_return

@app.get("/books/byrating/", status_code=200)
def read_books_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = [book for book in books if book.rating == book_rating]
    if not books_to_return:
        raise HTTPException(status_code=404, detail="No books found with this rating")
    return books_to_return

@app.get("/books/bypublishdate/", status_code=200)
def read_books_by_publish_date(published_date: int = Query(gt=1999, lt=2031)):
    books_to_return = [book for book in books if book.published_date == published_date]
    if not books_to_return:
        raise HTTPException(status_code=404, detail="No books found for this published date")
    return books_to_return

@app.post("/", status_code=201)
def create_book(book: Book):
    new_book = Book(
        id=uuid4(),  # Auto-generate a UUID for new books
        title=book.title,
        author=book.author,
        desc=book.desc,
        rating=book.rating,
        published_date=book.published_date,
    )
    books.append(new_book)
    return new_book

@app.put("/{book_id}", status_code=200)
def update_book(book_id: UUID, updated_book: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            updated_book.id = book_id  # Ensure the ID remains unchanged
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")

@app.delete("/{book_id}", status_code=204)
def delete_book(book_id: UUID):
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return
    raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")
