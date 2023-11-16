from aiogram import types
from loader import dp


@dp.message_handler(text="/go")
async def get_data(message: types.Message):
    await message.answer(f"{message.from_user.full_name}\n"
                         f"Здесь мы можем подставлять данные")