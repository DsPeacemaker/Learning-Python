import asyncio
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN, admin_id

#для работы с асинхронной библиоткой создаем поток
loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)#Доставка сообщений