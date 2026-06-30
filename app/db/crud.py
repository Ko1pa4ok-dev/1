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

def get_books(db: Session):
    """Получить все книги"""
    return db.query(models.Book).all()