from fastapi import FastAPI , HTTPException
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str=Field(min_length=1)
    author: str=Field(min_length=2,max_length=60)
    desc: str=Field(min_length=5,max_length=100)
    rating: int=Field(gt=-1,lt=101)
   
#@validator('phone_number')
 
books=[]

@app.get("/")
def read_api():
    return books

@app.post("/")
def create_book(book: Book):
    books.append(book)
    return book

@app.put("/{book_id}")
def update_book(book_id: UUID , book:Book):
    counter=0
    for x in books:
        counter+=1
        if x.id==book_id:
            books[counter-1] =book
            #the book is the bookname updated naem given by us
            return books[counter-1]
    raise HTTPException(
        status_code=404,detail=f"ID {book_id}: doesnt eist" )

@app.delete("/{id}")
def delete_book(id : UUID):
    counter=0
    for x in books:
        counter+=1
        if x.id==id:
            del books[counter-1]
            return f"ID:{id} deleted"
    raise HTTPException(status_code=404,detail="ID {id} doesnt exist")
