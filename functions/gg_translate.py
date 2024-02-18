from googletrans import Translator

def google_trans_en(text):
	tarjimon = Translator()
	tarjima = tarjimon.translate(text, src='en', dest='uz')
	return tarjima.text
