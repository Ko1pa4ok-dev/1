from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from app import schemas
from app.db import crud, db

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

# 1. Получить список всех книг (с опциональной фильтрацией по category_id)
@router.get("/", response_model=List[schemas.Book])
def read_books(category_id: Optional[int] = None, database: Session = Depends(db.get_db)):
    books = crud.get_books(database, category_id=category_id)
    return books

# 2. Получить книгу по её ID
@router.get("/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, database: Session = Depends(db.get_db)):
    db_book = crud.get_book(database, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return db_book

# 3. Создать новую книгу (с валидацией: проверяем, существует ли указанная категория)
@router.post("/", response_model=schemas.Book, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, database: Session = Depends(db.get_db)):
    # Проверяем бизнес-логику: существует ли категория, к которой привязывают книгу
    db_category = crud.get_category(database, category_id=book.category_id)
    if db_category is None:
        raise HTTPException(status_code=400, detail="Указанная категория не существует")
    
    return crud.create_book(
        database, 
        title=book.title, 
        description=book.description, 
        price=book.price, 
        category_id=book.category_id,
        url=book.url
    )

# 4. Обновить существующую книгу
@router.put("/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookCreate, database: Session = Depends(db.get_db)):
    # Если при обновлении меняется категория, проверяем её существование
    db_category = crud.get_category(database, category_id=book.category_id)
    if db_category is None:
        raise HTTPException(status_code=400, detail="Указанная категория не существует")

    db_book = crud.update_book(
        database,
        book_id=book_id,
        title=book.title,
        description=book.description,
        price=book.price,
        category_id=book.category_id,
        url=book.url
    )
    if db_book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return db_book

# 5. Удалить книгу
@router.delete("/{book_id}")
def delete_book(book_id: int, database: Session = Depends(db.get_db)):
    success = crud.delete_book(database, book_id=book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return {"message": "Книга успешно удалена"}