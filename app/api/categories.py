from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import schemas
from app.db import crud, db

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

# 1. Получить список всех категорий
@router.get("/", response_model=List[schemas.Category])
def read_categories(database: Session = Depends(db.get_db)):
    categories = crud.get_categories(database)
    return categories

# 2. Получить категорию по её ID
@router.get("/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, database: Session = Depends(db.get_db)):
    db_category = crud.get_category(database, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return db_category

# 3. Создать новую категорию
@router.post("/", response_model=schemas.Category, status_code=status.HTTP_201_CREATED)
def create_category(category: schemas.CategoryCreate, database: Session = Depends(db.get_db)):
    return crud.create_category(database, title=category.title)

# 4. Обновить существующую категорию
@router.put("/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, category: schemas.CategoryCreate, database: Session = Depends(db.get_db)):
    db_category = crud.update_category(database, category_id=category_id, title=category.title)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return db_category

# 5. Удалить категорию
@router.delete("/{category_id}")
def delete_category(category_id: int, database: Session = Depends(db.get_db)):
    success = crud.delete_category(database, category_id=category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return {"message": "Категория успешно удалена"}