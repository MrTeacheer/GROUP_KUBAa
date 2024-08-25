from aiogram import types, Dispatcher
from config import bot
import random

games = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']


async def send_game(m: types.Message):
    random_game=random.choice(games)
    await bot.send_dice(chat_id=m.from_user.id,
                        emoji=random_game)

def register_game(dp: Dispatcher):
    dp.register_message_handler(send_game,commands=['game'])