from fastapi import Body, FastAPI

app = FastAPI()
BOOKS = [
    {'title': 'tile 1', 'author': 'author1', 'category': 'scinece'},
    {'title': 'tile 2', 'author': 'author2', 'category': 'scinece'},
    {'title': 'tile 3', 'author': 'author3', 'category': 'scinece'},
    {'title': 'tile 4', 'author': 'author4', 'category': 'math'},
    {'title': 'tile 5', 'author': 'author3', 'category': 'history'}
]


@app.get("/books")
def read_all_books():
    return BOOKS
@app.get("/books/{book_title}")
def read_book(book_title : str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
@app.get("/books/")
def read_category_query (category : str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold()==category.casefold():
            books_to_return.append(book)
    return books_to_return
#place no.of parameteras end points in ascendingorder!
@app.get("/books/byauthor/")
def all_author_books(author_name : str):
    author_written_books = []
    for book in BOOKS:
        if book.get('author').casefold() == author_name.casefold():
            author_written_books.append(book)
    return author_written_books
@app.get("/books/{book_author}/")
def read_author_category_by_query(book_author: str, category : str):
    books_to_return =[]
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return
@app.post("/books/create_book")
def create_book(new_book = Body()):
    BOOKS.append(new_book)
@app.put("/books/update_book")
def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

@app.delete("/books/delete_book/{book_title}")
def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
@app.get("/books/byauthor/{author_name}")
def author_books(author_name : str):
    author_written_books = []
    for book in BOOKS:
        if book.get('author').casefold() == author_name.casefold():
            author_written_books.append(book)
    return author_written_books








'''
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001 '''
