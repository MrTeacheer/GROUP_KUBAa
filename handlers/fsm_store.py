import aiohttp
from aiogram import types, Dispatcher
from config import bot
import random
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from buttons import sizes
class Store(StatesGroup):
    name=State()
    size=State()
    category=State()
    price=State()
    photo=State()

size=['M','L']

async def start(message: types.Message):
    await message.answer('name of product?')
    await Store.name.set()

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer('size of product?',reply_markup=sizes)
    await Store.next()

async def load_size(message: types.Message, state: FSMContext):
    if message.text in size:
        kb = types.ReplyKeyboardRemove()
        async with state.proxy() as data:
            data['size'] = message.text
        await message.answer('category of product?', reply_markup=kb)
        await Store.next()
    else:
         await message.answer('pressonly buttons!!!')



async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
    await message.answer('price of product?')
    await Store.next()

async def load_price(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['price'] = message.text
        await message.answer('photo of product?')
        await Store.next()
    else:
        await message.answer('only digits!!!')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await message.answer_photo(photo=data['photo'],
                               caption=f'{data["name"]}\n'
                                       f'{data["size"]}\n'
                                       f'{data["category"]}\n'
                                       f'{data["price"]}')
    await state.finish()
def register_fsm_store(dp: Dispatcher):
    dp.register_message_handler(start, commands=['fsm_store'])
    dp.register_message_handler(load_name, state=Store.name)
    dp.register_message_handler(load_size, state=Store.size)
    dp.register_message_handler(load_category, state=Store.category)
    dp.register_message_handler(load_price, state=Store.price)
    dp.register_message_handler(load_photo, state=Store.photo,content_types=['photo'])
