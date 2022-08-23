from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token = '5056211474:AAHJugdsB6AfcIon9PlABUQsO4rSAkBNKUI')

dp = Dispatcher(bot)

@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = "Some text"

    await bot.send_message(chat_id= chat_id, text = text)

executor.start_polling(dp)




