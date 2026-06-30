from fastapi import FastAPI
from app.api import categories, books

# Создаем основной объект приложения FastAPI
app = FastAPI(
    title="Book Library API",
    description="API для управления каталогом книг и категорий",
    version="1.0.0"
)

# Простой эндпоинт для проверки работоспособности сервиса (healthcheck)
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "Сервис работает в штатном режиме"}

# Подключаем роутеры из папки app/api
app.include_router(categories.router)
app.include_router(books.router)
