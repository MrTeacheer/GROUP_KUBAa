from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import buttons
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import db
from handlers.fsm_store import start


class FSM_store(StatesGroup):
    name_product = State()
    size_product = State()
    price_product = State()
    id_product = State()
    category=State()
    info_product=State()
    photo_product = State()


async def fsm_start(message: types.Message):
    await FSM_store.name_product.set()
    await message.answer(text='Введите название товара: ')


async def load_name_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data_store:
        data_store['name_product'] = message.text

    await FSM_store.next()
    await message.answer(text='Укажите размер товара: ')


async def load_size_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data_store:
        data_store['size_product'] = message.text

    await FSM_store.next()
    await message.answer(text='Укажите цену товара: ')


async def load_price_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data_store:
        data_store['price_product'] = message.text

    await FSM_store.next()
    await message.answer(text='Укажите артикул товара: ')


async def load_id_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data_store:
        data_store['id_product'] = message.text

    await FSM_store.next()
    await message.answer(text='Напишите категорию товара:')

async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data_store:
        data_store['category'] = message.text
    await message.answer('info of product?')
    await FSM_store.next()

async def load_info_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data_store:
        data_store['info_product'] = message.text
    await message.answer('photo of product?')
    await FSM_store.next()

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data_store:
        data_store['photo'] = message.photo[-1].file_id

    await message.answer_photo(photo=data_store['photo'],
                               caption=f"Название товара - {data_store['name_product']}\n"
                                       f"Информация о товаре - {data_store['info_product']}\n"
                                       f"Категория - {data_store['category']}\n"
                                       f"Размер - {data_store['size_product']}\n"
                                       f"Цена - {data_store['price_product']}\n"
                                       f"Артикул - {data_store['id_product']}",
                               )
    await db.sql_insert_products(
        name=data_store['name_product'],
        size=data_store['size_product'],
        price=data_store['price_product'],
        id=data_store['id_product'],
        photo=data_store['photo'],
    )
    await db.sql_insert_products_detail(
        id=data_store['id_product'],
        category=data_store['category'],
        info=data_store['info_product']
    )
    await state.finish()


def store_fsm(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['product'])
    dp.register_message_handler(load_name_product, state=FSM_store.name_product)
    dp.register_message_handler(load_size_product, state=FSM_store.size_product)
    dp.register_message_handler(load_price_product, state=FSM_store.price_product)
    dp.register_message_handler(load_id_product, state=FSM_store.id_product)
    dp.register_message_handler(load_category, state=FSM_store.category)
    dp.register_message_handler(load_info_product,state=FSM_store.info_product)
    dp.register_message_handler(load_photo, state=FSM_store.photo_product, content_types=['photo'])
