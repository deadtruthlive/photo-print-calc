"""Модуль для взаимодействия с пользователем (ввод/вывод)."""

def get_print_params():
    """Запрашивает параметры печати у пользователя."""
    print("--- Параметры заказа ---")
    
    # Выбор формата
    print("Доступные форматы: 10x15, 13x18, A4, A3")
    photo_format = input("Введите формат: ").strip()
    
    # Выбор бумаги
    print("Тип бумаги: матовая, глянцевая")
    paper_type = input("Введите тип бумаги: ").strip().lower()
    
    # Ввод количества с проверкой
    while True:
        try:
            count = int(input("Введите количество фотографий: "))
            if count > 0:
                break
            print("Ошибка: Количество должно быть больше 0.")
        except ValueError:
            print("Ошибка: Введите целое число.")
            
    # Срочность
    is_urgent = input("Заказ срочный? (да/нет): ").strip().lower() == 'да'
    
    return {
        "format": photo_format,
        "paper": paper_type,
        "count": count,
        "urgent": is_urgent
    }

def print_receipt(data, total_price):
    """Выводит итоговый чек на экран."""
    print("\n" + "="*20)
    print("ИТОГОВЫЙ ЧЕК")
    print(f"Формат: {data['format']}")
    print(f"Бумага: {data['paper']}")
    print(f"Количество: {data['count']} шт.")
    print(f"Срочность: {'Да' if data['urgent'] else 'Нет'}")
    print("-" * 20)
    print(f"ИТОГО К ОПЛАТЕ: {total_price} руб.")
    print("="*20 + "\n")
