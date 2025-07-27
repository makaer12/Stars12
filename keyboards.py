# keyboards.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from utils import get_star_packages
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Купить Звёзды Telegram'))
    kb.add(KeyboardButton('Подарить Звёзды Telegram'))
    kb.add(KeyboardButton('Кошелёк'), KeyboardButton('Профиль'), KeyboardButton('FAQ'))
    return kb

def star_amounts_keyboard():
    kb = InlineKeyboardMarkup(row_width=2)
    for amount, price in get_star_packages():
        kb.add(InlineKeyboardButton(f"{amount} ⭐ ({price} RUB)", callback_data=f"buy_{amount}"))
    return kb

def update_rate_keyboard():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🔁 Обновить курс", callback_data="update_rate"))
    return kb

def payment_methods_keyboard():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("СПБ", callback_data="pay_spb"),
        InlineKeyboardButton("Банковская карта", callback_data="pay_card")
    )
    return kb

def wallet_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Пополнить баланс'), KeyboardButton('Вывести средства'))
    kb.add(KeyboardButton('История операций'), KeyboardButton('Назад'))
    return kb

def deposit_methods_keyboard():
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("СПБ", callback_data="deposit_spb"),
        InlineKeyboardButton("Банковская карта", callback_data="deposit_card")
    )
    return kb

def withdraw_methods_keyboard():
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("СПБ", callback_data="withdraw_spb"),
        InlineKeyboardButton("Банковская карта", callback_data="withdraw_card")
    )
    return kb

def profile_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Назад'))
    return kb