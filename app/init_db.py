from app.db.db import engine, Base, SessionLocal
from app.db import crud

def init_database():
    print("Создание таблиц в базе данных...")
    # Эта команда автоматически создаст таблицы categories и books на основе моделей
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        # Проверяем, если категории уже созданы, чтобы не дублировать
        existing_categories = crud.get_categories(db)
        if not existing_categories:
            print("Заполнение базы данных тестовыми данными...")
            
            # Добавляем 2 категории товара
            cat_programming = crud.create_category(db, title="Программирование")
            cat_fiction = crud.create_category(db, title="Художественная литература")
            
            # Добавляем книги к первой категории (Программирование)
            crud.create_book(
                db, 
                title="Изучаем Python", 
                description="Классический учебник Марка Лутца по языку Python.", 
                price=1250.0, 
                category_id=cat_programming.id
            )
            crud.create_book(
                db, 
                title="Чистый код", 
                description="Руководство по созданию хорошего кода от Роберта Мартина.", 
                price=950.0, 
                category_id=cat_programming.id
            )
            
            # Добавляем книги ко второй категории (Художественная литература)
            crud.create_book(
                db, 
                title="1984", 
                description="Знаменитый роман-антиутопия Джорджа Оруэлла.", 
                price=450.0, 
                category_id=cat_fiction.id
            )
            crud.create_book(
                db, 
                title="Мастер и Маргарита", 
                description="Шедевр Михаила Булгакова.", 
                price=600.0, 
                category_id=cat_fiction.id
            )
            
            print("База данных успешно инициализирована и заполнена!")
        else:
            print("База данных уже содержит данные, повторное заполнение не требуется.")
            
    except Exception as e:
        print(f"Произошла ошибка при инициализации БД: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    init_database()