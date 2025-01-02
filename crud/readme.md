
# FastAPI Book Management API

A simple Book Management API built with FastAPI, enabling CRUD operations for managing books. This project demonstrates basic functionality such as retrieving, creating, updating, and deleting book records.

## Features

- **Retrieve All Books:** Fetch all books in the collection.
- **Retrieve a Single Book:** Fetch details of a specific book by its ID.
- **Add a New Book:** Add a new book to the collection.
- **Update Book Details:** Update specific or all details of a book.
- **Delete a Book:** Remove a book from the collection.

## Endpoints

### 1. Get All Books
```http
GET /books
```
- Response: List of all books.

### 2. Get a Book by ID
```http
GET /book/{book_id}
```
- Response: Details of the specified book.
- Error: `404 Not Found` if the book doesn't exist.

### 3. Add a New Book
```http
POST /books
```
- Request Body: Book details (title, author, publisher, etc.)
- Response: Newly created book.

### 4. Update Book Details
```http
PATCH /book/{book_id}
```
- Request Body: Partial or complete book details.
- Response: Updated book details.
- Error: `404 Not Found` if the book doesn't exist.

### 5. Delete a Book
```http
DELETE /book/{book_id}
```
- Response: Empty body with `204 No Content`.
- Error: `404 Not Found` if the book doesn't exist.

## Data Models

### Book Model
```json
{
  "id": 1,
  "title": "Example Book Title",
  "author": "Author Name",
  "publisher": "Publisher Name",
  "page_count": 100,
  "language": "English"
}
```

### UpdateBook Model
- Supports optional fields for partial updates.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fastapi-book-management.git
   cd fastapi-book-management
   ```

2. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

3. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

4. Open your browser and navigate to:
   - API Documentation: `http://127.0.0.1:8000/docs`
   - ReDoc Documentation: `http://127.0.0.1:8000/redoc`

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (ASGI server)

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this project as per the license terms.

---

Feel free to contribute by submitting issues or pull requests!
```
