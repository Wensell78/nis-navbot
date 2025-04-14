from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
import asyncio

bot = Bot(token='7505011610:AAEhUgTx9QiG51djCtN8DhNElk42XEwZBa8')
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def main(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Найти кабинет'))
    builder.add(types.KeyboardButton(text='Расписание'))
    builder.adjust(2)  # Располагаем кнопки в 2 колонки
    
    await message.answer(
        f'Привет, {message.from_user.first_name}, я - бот-навигатор по школе! Чем могу помочь?',
        reply_markup=builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
    )

# Обработчик текстовых сообщений
@dp.message()
async def on_click(message: types.Message):
    if message.text == 'Найти кабинет':
        await message.answer('Окей, я помогу найти тебе нужный кабинет. Возле какого ты сейчас находишься?')
    elif message.text.lower() == 'фм101':
        await message.reply('Отлично! Куда направимся?')
    elif message.text == 'Расписание':
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text='Расписание', 
            url='https://niskaraganda.edupage.org/timetable/'
        ))
        await message.answer('Держи!', reply_markup=builder.as_markup())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())