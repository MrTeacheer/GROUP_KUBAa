import sqlite3
from . import queries
db = sqlite3.connect('db.sqlite3')
cursor = db.cursor()


async def sql_create():
    if db:
        print("База данных SQLite3 подключена!")

    cursor.execute(queries.CREATE_TABLE_PRODUCTS)
    cursor.execute(queries.CREATE_TABLE_PRODUCT_DETAIL)
    cursor.execute(queries.CREATE_TABLE_COLLECTION)
    db.commit()


async def sql_insert_products(name,size,price,id,photo):
    if db:
        cursor.execute(queries.INSERT_INTO_PRODUCTS,(None,name,size,price,id,photo))
    db.commit()

async def sql_insert_products_detail(id,category,info):
    if db:
        cursor.execute(queries.INSERT_INTO_PRODUCTS_DETAIL,(None,id,category,info))
    db.commit()

async def sql_insert_collection(id,collection):
    if db:
        cursor.execute(queries.INSERT_INTO_COLLECTION,(None,id,collection))
    db.commit()