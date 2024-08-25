from aiogram.types import document

from config import bot,dp
from aiogram import types, Dispatcher


async def pin(message: types.Message):
    if message.chat.type != 'private':
        if message.reply_to_message:
            pinmes=message.reply_to_message
            await bot.pin_chat_message(message.chat.id,pinmes.message_id)
        else:
            await message.answer('couldnt pin')
    else:
        await message.answer('works oonly in groups')


def registr_group(dp: Dispatcher):
    dp.register_message_handler(pin, text='!pin')