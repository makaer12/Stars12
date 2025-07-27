from aiogram import Router, types, F

router = Router()

@router.message(F.text == "Профиль")
async def profile_entry(message: types.Message):
    await message.answer(
        f"👤 Ваш профиль\nTelegram ID: {message.from_user.id}\nБаланс: 0.00 RUB\nУровень доверия: 1\nРейтинг: 5.0\nЗавершённых сделок: 0"
    )