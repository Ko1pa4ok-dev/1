from app.db.db import SessionLocal
from app.db import crud

def main():
    print("=== ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ POSTGRESQL ===")
    db = SessionLocal()
    try:
        # Читаем данные из таблиц через CRUD функции
        categories = crud.get_categories(db)
        books = crud.get_books(db)
        
        print(f"\nНайдено категорий в БД: {len(categories)}")
        print("-" * 40)
        for cat in categories:
            print(f"ID: {cat.id} | Категория: {cat.title}")
            
        print(f"\nНайдено книг в БД: {len(books)}")
        print("-" * 40)
        for book in books:
            # Получаем название категории для книги
            category_name = book.category_rel.title if book.category_rel else "Без категории"
            print(f"Книга: \"{book.title}\"")
            print(f"  Описание: {book.description}")
            print(f"  Цена: {book.price} руб.")
            print(f"  Категория: {category_name}")
            print("." * 30)
            
    except Exception as e:
        print(f"Ошибка при чтении данных из БД: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
