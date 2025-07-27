from aiogram import Router, types, F

router = Router()

@router.message(F.text == "Кошелёк")
async def wallet_entry(message: types.Message):
    await message.answer("💼 Ваш баланс: 0.00 RUB\nВыберите действие:\nПополнить баланс / Вывести средства / История операций")