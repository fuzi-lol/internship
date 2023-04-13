from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()
class Book:

    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int
    def __init__(self, id, title, author, description, rating,published_date):
        self.id = id
        self.title = title
        self.description = description
        self.author = author
        self.rating = rating
        self.published_date= published_date
class Bookrequest(BaseModel):

    id: Optional[int] =Field(title=" id is optional")
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(lt=6, gt=0)
    published_date: int = Field( lt=31, gt=0)

    class Config:
        schema_extra = {
            'example': {
                'title' : 'a new  book',
                'author': "fuzi",
                'description' : 'a new description book',
                'rating': 4,
                'published_date' : 23

            }
        }




BOOKS =[
    Book(1, 'computer science pro', 'coding with fuzi', 'a very nice book', 5, 23),
    Book(2, 'Be Fast with api', 'coding with fuzi', 'a very nice book', 5, 24),
    Book(3, 'master endpoints', 'coding with fuzi', 'a very nice book', 5, 25),
    Book(4, 'hp1', 'author1', 'Book Description', 2, 26),
    Book(5, 'hp2', 'author2', 'Book Description', 3, 27),
    Book(6, 'hp3', 'author3', 'Book Description', 1, 28),
]
@app.get("/books")
def read_all_books():
    return BOOKS

@app.get("/books/{bookid}")
def read_book( bookid: int):
    for book in BOOKS:
        if book.id == bookid :
            return book

@app.get("/books/")
def read_book_by_rating(book_rating: int):
    books_to_return =[]
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.post("/create_book")
async def create_book(book_request: Bookrequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book : Book):
    if len(BOOKS)>0:
        book.id = BOOKS[-1].id+1
    else:
        book.id =1
    return book
@app.put("/books/update_book")
def update_book(book : Bookrequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] =book
@app.delete('/books/{book_id}/')
def delete_book(book_id : int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
@app.get("/books/by_published_date/")
def published_date(publishedDate: int):
    bookstoreturn = []
    for book in BOOKS:
        if book.published_date == publishedDate:
            bookstoreturn.append(book)
    return bookstoreturn


