from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

service_btn = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton(text = '📄 Text')
		],
		[
			KeyboardButton(text = 'ℹ️ INFO')	
		]
	],
	resize_keyboard = True
	)