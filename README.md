My journey of learning FASTAPI .
From basics to building web apps along with Pydantic for data validation.
The learning is done with the help of [Eric Roby](https://www.youtube.com/playlist?list=PLK8U0kF0E_D6l19LhOGWhVZ3sQ6ujJKq)

1.Books.py
# Book Management API with FastAPI

This project is a simple FastAPI application to manage a collection of books using in-memory storage. It demonstrates CRUD operations and data validation.

## Features

1. **Book Model**: 
   - `id` (UUID): Unique identifier for each book.
   - `title` (string): Book title (min length: 1 character).
   - `author` (string): Author name (2–60 characters).
   - `desc` (string): Book description (5–100 characters).
   - `rating` (integer): Book rating (0–100).

2. **API Endpoints**:
   - `GET /`: Fetches the list of all books.
   - `POST /`: Adds a new book to the collection.
   - `PUT /{book_id}`: Updates details of a book by its `UUID`.
   - `DELETE /{id}`: Deletes a book by its `UUID`.

3. **Validation**:
   - Input data is validated using `pydantic`'s `Field()` constraints.
   - Ensures required formats and lengths for fields like `title`, `author`, `desc`, and `rating`.

4. **Error Handling**:
   - If a book's `UUID` is not found during updates or deletions, a `404 Not Found` error is raised using `HTTPException`.

This API is designed for learning purposes and currently uses in-memory storage for simplicity.
