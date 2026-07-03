from sqlalchemy.orm import Session
from app.db import models

# --- Операции для Категорий ---
def create_category(db: Session, title: str):
    """Создать новую категорию"""
    db_category = models.Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()
    
def get_categories(db: Session):
    """Получить все категории"""
    return db.query(models.Category).all()

def update_category(db: Session, category_id: int, title: str):
    """Обновить название категории"""
    db_category = get_category(db, category_id)
    if db_category:
        db_category.title = title
        db.commit()
        db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    """Удалить категорию"""
    db_category = get_category(db, category_id)
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category

# --- Операции для Книг ---
def create_book(db: Session, title: str, description: str, price: float, category_id: int, url: str = ""):
    db_book = models.Book(
        title=title,
        description=description,
        price=price,
        category_id=category_id,  # <-- Проверь, чтобы тут было чётко category_id=category_id
        url=url
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_book(db: Session, book_id: int):
    """Получить одну книгу по ID"""
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_book(db: Session, book_id: int, title: str = None, description: str = None, price: float = None):
    """Обновить данные книги"""
    db_book = get_book(db, book_id)
    if db_book:
        if title: db_book.title = title
        if description: db_book.description = description
        if price: db_book.price = price
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    """Удалить книгу"""
    db_book = get_book(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book