from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

# Button
from keyboards.keyboard import service_btn

rtr = Router()

@rtr.message(CommandStart())
async def start_command(message: Message):
	await message.answer(text=f"👋 Assalomu alaykum!\n👇 Quyidagilardan birini tanlang!", reply_markup = service_btn)

@rtr.message(Command('help'))
async def help_command(message: Message):
	await message.answer(text=f"Bu bot orqali ingliz tili matndagi so'zlarni lug'at ko'rinishida olishingiz mumkin!", reply_markup = service_btn)