import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from config import TOKEN # This is bot token
from handlers.commands import rtr
from handlers.service import svc_rtr

async def main():
	bot = Bot(token=TOKEN)
	dp = Dispatcher()
	dp.include_routers(rtr, svc_rtr)
	await dp.start_polling(bot)

if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO, stream=sys.stdout)
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		print("Bot stopped")

