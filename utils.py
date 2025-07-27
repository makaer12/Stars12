# utils.py
from config import BASE_RATE, SELL_MARGIN, COMPETITOR_RATE, STAR_AMOUNTS

def get_current_sell_rate():
    """Рассчитать актуальный курс продажи одной звезды."""
    return min(BASE_RATE + SELL_MARGIN, COMPETITOR_RATE - 0.01)

def get_star_packages():
    """Вернуть список пакетов звёзд и их цены по актуальному курсу."""
    rate = get_current_sell_rate()
    return [(amount, round(amount * rate, 2)) for amount in STAR_AMOUNTS]