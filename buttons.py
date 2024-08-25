from aiogram import types

sizes=types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton('L'),
                                                          types.KeyboardButton('M'))

link='https://online.geeks.kg/'
web=types.WebAppInfo(url=link)
urls=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text='geeks',web_app=web),
                                      types.InlineKeyboardButton(text='geeks',web_app=web),
                                      types.InlineKeyboardButton(text='geeks',web_app=web),
                                      types.InlineKeyboardButton(text='geeks',web_app=web),
                                      types.InlineKeyboardButton(text='geeks',web_app=web))