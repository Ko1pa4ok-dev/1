from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)  # Название категории

    # Связь с книгами: одна категория может содержать много книг
    books = relationship("Book", back_populates="category_rel", cascade="all, delete-orphan")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)        # Название книги
    description = Column(String, nullable=True)   # Описание книги
    price = Column(Float, nullable=False)         # Цена книги
    url = Column(String, nullable=True, default="") # Ссылка на товар (пока пустая)
    
    # Внешний ключ, указывающий на id категории
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)

    # Обратная связь с категорией
    category_rel = relationship("Category", back_populates="books")