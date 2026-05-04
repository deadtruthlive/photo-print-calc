"""Модуль для выполнения математических расчетов стоимости заказа."""

def calculate_base_price(count, format_price):
    """Рассчитывает базовую стоимость без учета скидок."""
    return count * format_price
