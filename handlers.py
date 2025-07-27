# handlers/wallet.py
from aiogram import types, Dispatcher
from models import get_user, add_balance, get_user_transactions, get_user_profile
from keyboards import wallet_menu, deposit_methods_keyboard, withdraw_methods_keyboard, profile_menu
from messages import (
    wallet_main, deposit_choose_method, withdraw_choose_method,
    deposit_success, withdraw_success, not_enough_funds,
    history_title, transaction_line, profile_message
)

async def wallet_entry(message: types.Message):
    user = get_user(message.from_user.id)
    await message.answer(wallet_main(user["balance"]), reply_markup=wallet_menu())

async def wallet_deposit(message: types.Message):
    await message.answer(deposit_choose_method(), reply_markup=deposit_methods_keyboard())

async def deposit_method_chosen(callback_query: types.CallbackQuery):
    # Здесь будет интеграция с оплатой
    # Пока — просто пополнение на тестовую сумму
    tx = add_balance(callback_query.from_user.id, 1000.0, "deposit", "Тестовое пополнение")
    await callback_query.message.answer(deposit_success(tx["amount"]))

async def wallet_withdraw(message: types.Message):
    await message.answer(withdraw_choose_method(), reply_markup=withdraw_methods_keyboard())

async def withdraw_method_chosen(callback_query: types.CallbackQuery):
    user = get_user(callback_query.from_user.id)
    if user["balance"] < 100:
        await callback_query.message.answer(not_enough_funds())
    else:
        tx = add_balance(callback_query.from_user.id, -100.0, "withdraw", "Тестовый вывод")
        await callback_query.message.answer(withdraw_success(-tx["amount"]))

async def wallet_history(message: types.Message):
    txs = get_user_transactions(message.from_user.id, limit=10)
    if not txs:
        await message.answer("Нет операций.")
    else:
        text = history_title() + "\n" + "\n".join([transaction_line(tx) for tx in txs])
        await message.answer(text)

def register_wallet_handlers(dp: Dispatcher):
    dp.register_message_handler(wallet_entry, lambda m: m.text == "Кошелёк")
    dp.register_message_handler(wallet_deposit, lambda m: m.text == "Пополнить баланс")
    dp.register_callback_query_handler(deposit_method_chosen, lambda c: c.data.startswith("deposit_"))
    dp.register_message_handler(wallet_withdraw, lambda m: m.text == "Вывести средства")
    dp.register_callback_query_handler(withdraw_method_chosen, lambda c: c.data.startswith("withdraw_"))
    dp.register_message_handler(wallet_history, lambda m: m.text == "История операций")

    async def profile_entry(message: types.Message):
        profile = get_user_profile(message.from_user.id)
        await message.answer(profile_message(profile), reply_markup=profile_menu())

    def register_profile_handlers(dp: Dispatcher):
        dp.register_message_handler(profile_entry, lambda m: m.text == "Профиль")