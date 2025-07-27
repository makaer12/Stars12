# main.py
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from handlers.wallet import register_wallet_handlers]
from handlers.profile import register_profile_handlers
from config import BOT_TOKEN, COMPETITOR_RATE
from keyboards import main_menu, star_amounts_keyboard, update_rate_keyboard, payment_methods_keyboard
from messages import balance_message, choose_amount_message, package_selected_message, rate_message
from utils import get_current_sell_rate, get_star_packages

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Пример простой базы для баланса
user_balances = {}

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    user_balances.setdefault(user_id, 0)
    await message.answer(balance_message(user_balances[user_id]), reply_markup=main_menu())

@dp.message_handler(lambda msg: msg.text == "Купить Звёзды Telegram")
async def buy_stars(message: types.Message):
    await message.answer(choose_amount_message(), reply_markup=star_amounts_keyboard())

@dp.callback_query_handler(lambda c: c.data and c.data.startswith("buy_"))
async def process_buy_amount(callback_query: types.CallbackQuery):
    amount = int(callback_query.data.split("_")[1])
    rate = get_current_sell_rate()
    price = round(amount * rate, 2)
    await callback_query.message.answer(package_selected_message(amount, price), reply_markup=payment_methods_keyboard())

@dp.callback_query_handler(lambda c: c.data == "update_rate")
async def update_rate(callback_query: types.CallbackQuery):
    rate = get_current_sell_rate()
    await callback_query.message.answer(rate_message(rate, COMPETITOR_RATE))

    if __name__ == "__main__":
        register_wallet_handlers(dp)
        register_profile_handlers(dp)
        executor.start_polling(dp, skip_updates=True)