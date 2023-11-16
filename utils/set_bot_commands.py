from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("go", "Получить данные"),
            types.BotCommand("geo_pos", "Получить координаты"),
            types.BotCommand("help", "Вывести справку"),

        ]
    )
