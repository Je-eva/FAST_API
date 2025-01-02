from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List,Optional

app = FastAPI()


books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-19",
        "page_count": 1023,
        "language": "English",
    },
    {
        "id": 3,
        "title": "The web socket handbook",
        "author": "Alex Diaconu",
        "publisher": "Xinyu Wang",
        "published_date": "2021-01-01",
        "page_count": 3677,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Head first Javascript",
        "author": "Hellen Smith",
        "publisher": "Oreilly Media",
        "published_date": "2021-01-01",
        "page_count": 540,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Algorithms and Data Structures In Python",
        "author": "Kent Lee",
        "publisher": "Springer, Inc",
        "published_date": "2021-01-01",
        "page_count": 9282,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Head First HTML5 Programming",
        "author": "Eric T Freeman",
        "publisher": "O'Reilly Media",
        "published_date": "2011-21-01",
        "page_count": 3006,
        "language": "English",
    },
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


# Pydantic model for book update
class UpdateBook(BaseModel):
    title: Optional[str] = None
    publisher: Optional[str] = None
    page_count: Optional[int] = None
    language: Optional[str] = None
    author: Optional[str] = None


#tis one is  one not having pydantic validation
@app.get("/books")
async def get_all_books():
    return books

#since its a list.. but puydantic walways wants dicitonary. so intenra; server ccurs, hence List[Books] used
@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books


@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book):
    new_book = book_data.model_dump()
    #sepcial append methoid
#aceesing bookdata as dictinoary

    books.append(new_book)

    return new_book

@app.get("/book/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

#using optinal 
@app.patch("/book/{book_id}")
async def update_book(book_id: int, book_update_data: UpdateBook):
    for book in books:
        if book['id'] == book_id:
            # Update only fields that are provided in the request
            if book_update_data.title is not None:
                book['title'] = book_update_data.title
            if book_update_data.publisher is not None:
                book['publisher'] = book_update_data.publisher
            if book_update_data.page_count is not None:
                book['page_count'] = book_update_data.page_count
            if book_update_data.language is not None:
                book['language'] = book_update_data.language
            if book_update_data.author is not None:
                book['author'] = book_update_data.author

            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

#making it to be a update comulsary on all tables as neccesaary. 
@app.patch("/book/{book_id}")
async def update_book(book_id: int,book_update_data:UpdateBook):
    
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['publisher'] = book_update_data.publisher
            book['page_count'] = book_update_data.page_count
            book['language'] = book_update_data.language
            book['atuhor'] = book_update_data.author
            

            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")



@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:  
        if book["id"] == book_id:
#target tje sepcify tjat book doctopamry amd removei t using puthon.
            books.remove(book)
            return {}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")