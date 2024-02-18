from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from time import perf_counter
# button
from keyboards.keyboard import service_btn

# states
from states.dic_states import DicStates

# function
from functions.gg_translate import google_trans_en

svc_rtr = Router()

@svc_rtr.message(F.text == '📄 Text')
async def text_to_translate(message: Message, state: FSMContext):
	await message.answer('Ingliz tilidagi matn yuboring!')
	await state.set_state(DicStates.dictext)
	
@svc_rtr.message(DicStates.dictext)
async def reg_name(message: Message, state=FSMContext):
	text = set((message.text).split())
	len_text = len(text)
	await message.answer(f'Kuting...⌛')
	msg = f"✅English --- ✅Uzbek\n\n"
	translate_word_count = 0
	for word in text:
		if len(word) >= 3 and word.isalpha():
			uz_word = google_trans_en(word).lower()
			if word.lower() != uz_word:
				translate_word_count += 1
				msg += f"{word.lower()} --- {uz_word}\n"
	msg += f"\n🤖 @TeleTarjimon_Bot"

	if translate_word_count != 0:
		await message.answer(msg, reply_markup = service_btn)
	else:
		await message.answer(f"✅English --- ✅Uzbek\n\n⊙﹏⊙∥ 🤷‍♂\n\n🤖 @TeleTarjimon_Bot")

	await state.clear()

@svc_rtr.message(F.text == 'ℹ️ INFO')
async def text_to_translate(message: Message):
	await message.answer('📅 Data: 18/02/2024 \n\n🧑‍💻 Programmer: @sunnatillo_coder')