import time
import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN, admin_id

MSG = "Программировал ли ты сегодня, {}?"
HATE = "Ну ты {} шершень! Бегом программировать!"
FINE = "Молодец, {}, горжусь тобой!"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler()
async def start_nandler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id}, {user_full_name}, {time.asctime()}')
    if message.text == 'Нет':
        await bot.send_message(user_id, HATE.format(user_name))
        await bot.send_photo(user_id, "https://trendymen.ru/images/article1/134214/prev1134214.jpg")
    elif message.text == 'Да':
        await bot.send_message(user_id, FINE.format(user_name))
        await bot.send_photo(user_id, "https://funart.pro/uploads/posts/2021-07/1625692181_22-funart-pro-p-kotik-laik-zhivotnie-krasivo-foto-46.jpg")
    else:
        await message.reply(f"Привет, {user_full_name}")

    for i in range(7):
        await bot.send_message(user_id, MSG.format(user_name))
        await asyncio.sleep(60*60*24)


if __name__ == '__main__':
    executor.start_polling(dp)