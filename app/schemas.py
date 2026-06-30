from pydantic import BaseModel, ConfigDict
from typing import Optional, List

# --- СХЕМЫ ДЛЯ КАТЕГОРИЙ ---

# Базовая схема для категории (то, что общее)
class CategoryBase(BaseModel):
    title: str

# Схема для создания/обновления категории (передаем только название)
class CategoryCreate(CategoryBase):
    pass

# Схема для ответа API (возвращаем клиенту вместе с ID)
class Category(CategoryBase):
    id: int
    
    # Включаем поддержку работы с моделями SQLAlchemy (раньше это называлось orm_mode)
    model_config = ConfigDict(from_attributes=True)


# --- СХЕМЫ ДЛЯ КНИГ ---

# Базовая схема для книги
class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    category_id: int
    url: Optional[str] = ""

# Схема для создания/обновления книги
class BookCreate(BookBase):
    pass

# Схема для ответа API (возвращаем книгу со всеми полями и ID)
class Book(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)