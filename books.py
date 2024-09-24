from book import BOOKS
from fastapi import FastAPI, Body

app = FastAPI()

# Example for 'GET' method
@app.get('/books')
async def fetch_all_books():
    return BOOKS


# Example for 'GET' method with dynamic path parameters
@app.get('/books/{book_title}')
async def fetch_book_by_book_title(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


# Example for 'GET' method with query parameters
@app.get('/books/')
async def fetch_books_by_category(category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return



# Example for 'GET' method with dynamic path parameters and query parameters
@app.get('/books/{book_author}/')
async def fetch_books_by_author_and_category(book_author:str,category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


# Example for 'POST' method
@app.post('/books/add-book')
async def add_book(new_book=Body()):
    BOOKS.append(new_book)


# Example for 'PUT' method
@app.put('/books/update_book')
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i]=updated_book


# Example for 'DELETE' method
@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

