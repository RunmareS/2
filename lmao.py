from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN_API = '7093886066:AAF1yQ45JUvF-XwMCqlez1bnuYjbkNuBPts'
bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command="/start", description= 'Начать работу бота'),
        types.BotCommand(command="/help", description='Помочь'),
        types.BotCommand(command="/about", description='Про бота'),
        types.BotCommand(command="/ask", description='Спросить')
    ]
    await bot.set_my_commands(commands)
@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.reply('Здарова, пдрила', reply_markup= keyboard1)
@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Иди к своему Артему Графу, тут Данила Граф я выкупил этот канал.')

@dp.message_handler(commands='about')
async def help(message: types.Message):
    await message.reply('Лучший бот буллинга над карликами (Джарахов)')

@dp.message_handler(commands='ask')
async def help(message: types.Message):
    await message.reply('Ну я хззз мб джарахов??')
keyboard1 = InlineKeyboardMarkup(row_width=3)
@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message.text)
async  def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor .start_polling(dp, skip_updates=True, on_startup= on_startup)