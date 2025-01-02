from fastapi import FastAPI
from routes import book_router

version = 'v1'

app = FastAPI(
    version= version,

    title="Bookly",
    description="A REST API for a book review web service")

app.include_router(book_router, prefix=f"/api/{version}/books",tags=['books'])