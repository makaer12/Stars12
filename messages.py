# messages.py

def balance_message(balance):
    return (
        f"Ваш баланс: {balance} ⭐\n\n"
        "Пожалуйста, используйте кнопки ниже, чтобы Купить Звёзды себе или 🎁 Подарить их Вашим друзьям."
    )

def choose_amount_message():
    return "Пожалуйста, нажмите на кнопку с нужным количеством Звёзд Telegram:"

def package_selected_message(amount, price):
    return f"Вы выбрали {amount} ⭐ за {price} RUB.\nВыберите способ оплаты:"

def rate_message(rate, competitor_rate):
    return (
        f"Текущий курс: {rate:.2f} RUB за 1 ⭐\n"
        f"Курс в PremiumBot: {competitor_rate:.2f} RUB\n"
        "Нажмите «🔁 Обновить курс», чтобы получить актуальные данные."
    )

def wallet_main(balance):
    return (
        f"💼 Ваш баланс: {balance:.2f} RUB\n"
        "Выберите действие:"
    )

def deposit_choose_method():
    return "Выберите способ пополнения:"

def withdraw_choose_method():
    return "Выберите способ вывода:"

def deposit_success(amount):
    return f"Баланс успешно пополнен на {amount:.2f} RUB!"

def withdraw_success(amount):
    return f"Вывод {amount:.2f} RUB успешно оформлен! Ожидайте подтверждения."

def not_enough_funds():
    return "Недостаточно средств для вывода."

def history_title():
    return "История ваших последних операций:"

def transaction_line(tx):
    sign = "+" if tx["amount"] > 0 else ""
    return f"{tx['timestamp']} | {sign}{tx['amount']:.2f} RUB | {tx['type']} | {tx.get('comment', '')}"

def profile_message(profile):
    return (
        f"👤 Ваш профиль\n"
        f"Telegram ID: {profile['telegram_id']}\n"
        f"Баланс: {profile['balance']:.2f} RUB\n"
        f"Уровень доверия: {profile['trust_level']}\n"
        f"Рейтинг: {profile['rating']:.1f}\n"
        f"Завершённых сделок: {profile['deals_completed']}\n"
    )