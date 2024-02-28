from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import random

def random_photo(a):
    photo=["https://neyrosety.ru/wp-content/uploads/2023/03/00585-3626125850-576x1024.jpg",
          "https://i.pinimg.com/736x/64/5b/bf/645bbf05cd95f6d4b1f8bb773d35bfcb.jpg",
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqw1faqzl_dDkaiuMxLsikBWFszg-T3y0_Hw&usqp=CAU",
          "https://img.freepik.com/premium-photo/pretty-phone-wallpaper_759095-116097.jpg",
          "https://i.pinimg.com/564x/59/8d/5e/598d5e7e2f1e878f9f3ccab792a97ab1.jpg",
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTqABx1QZvj-6Q_AHG3ujemwP5p830jVHZFw&usqp=CAU",
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjgrmw5KA_jEr6Etyc804GatcLGT8NBi2HJA&usqp=CAU",
          "https://masterpiecer-images.s3.yandex.net/15c7ff7b7a8811eeab4ada477c0f1ee2:upscaled",
          "https://www.meme-arsenal.com/memes/02cf7150ccb8e9732c39d5fc60e92643.jpg",
          "https://wallpapershome.ru/images/pages/pic_h/14540.jpg"]
    return photo[a]

TOKEN = "6271690788:AAHmUGEw3t9RLt6PsvPFSj37w8E94UJy_rw"

HELP_COM="""
/start - начало работы
/help - описание всех команд
/next - следующая картинка
"""
a=0
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_help = types.KeyboardButton('/help')
    button_next = types.KeyboardButton('/next')
    button_start = types.KeyboardButton('/start')
    keyboard.add(button_start)
    keyboard.add(button_next)
    keyboard.add(button_help)
    await message.reply("Привет! Это лента как в Инстаграмме.", reply_markup=keyboard)
    await message.reply(HELP_COM)
    await message. delete()

@dp.message_handler(commands=['help'])
async def next(message: types.Message):
    await message.reply(HELP_COM)
    await message. delete()

@dp.message_handler(commands=['next'])
async def next(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text="👍", callback_data="like")
    ib2 = InlineKeyboardButton(text="👎", callback_data="dislike")
    ikb.add(ib1,ib2)
    await bot. send_photo(chat_id=message.chat.id, photo=random_photo(random.randint(0,9)), reply_markup = ikb)
    await message. delete()

@dp.callback_query_handler()
async def callback(callback: types.CallbackQuery):
    if callback.data=="like":
        await callback.answer(text="Лайк поставлен")
    elif callback.data=="dislike":
        await callback.answer(text="Дизлайк поставлен")

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)
    await message. delete()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
