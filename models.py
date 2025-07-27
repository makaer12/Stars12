# models.py
from typing import List, Dict
from datetime import datetime
from typing import Optional
# Простой in-memory storage (заменить на БД в бою)
USERS: Dict[int, dict] = {}
TRANSACTIONS: List[dict] = []

def get_user(user_id: int):
    if user_id not in USERS:
        USERS[user_id] = {
            "balance": 0.0,
            "transactions": []
        }
    return USERS[user_id]

def add_balance(user_id: int, amount: float, type_: str, comment: str = ""):
    user = get_user(user_id)
    user["balance"] += amount
    tx = {
        "user_id": user_id,
        "amount": amount,
        "type": type_,  # "deposit", "withdraw", "buy", "gift"
        "comment": comment,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    user["transactions"].append(tx)
    TRANSACTIONS.append(tx)
    return tx

def get_user_transactions(user_id: int, limit=10):
    return get_user(user_id)["transactions"][-limit:]

def get_user_profile(user_id: int):
    user = get_user(user_id)
    # Примерные метрики (можно доработать под реальные)
    profile = {
        "telegram_id": user_id,
        "balance": user["balance"],
        "trust_level": user.get("trust_level", 1),
        "rating": user.get("rating", 5.0),
        "deals_completed": sum(1 for tx in user["transactions"] if tx["type"] == "buy"),
    }
    return profile

def increment_deals(user_id: int):
    user = get_user(user_id)
    user["deals_completed"] = user.get("deals_completed", 0) + 1

def set_trust_level(user_id: int, level: int):
    user = get_user(user_id)
    user["trust_level"] = level

def set_rating(user_id: int, rating: float):
    user = get_user(user_id)
    user["rating"] = rating