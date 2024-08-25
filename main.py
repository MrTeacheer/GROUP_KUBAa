from aiogram import executor
from config import bot,dp
from database import db
from handlers import (start,
                      echo,
                      commands,
                      quiz,
                      game,
                      fsm_store,
                      fsm_kuba)

async def on_startup(_):
    await db.sql_create()

start.register_start(dp=dp)
commands.register_commands(dp=dp)
quiz.register_quiz(dp=dp)
game.register_game(dp=dp)
fsm_store.register_fsm_store(dp=dp)
fsm_kuba.store_fsm(dp=dp)
echo.register_echo(dp=dp)







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,on_startup=on_startup)