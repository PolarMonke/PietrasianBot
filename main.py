import telebot
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
COPYPASTA = '''
Ты здзекуешся ??? Што за ***** ты вярзеш, чал ? Ты найбольшы няўдаха, якога я бачыў у жыцці ! Ты рабіў ПІПІ ў свае памперсы, пакуль я перамагаў гульцоў нашмат мацнейшых за цябе! Ты не прафесіянал, бо прафесіяналы ўмеюць прайграваць і віншаваць апанентаў, а ты як дзяўчынка, што плача пасля таго, як я цябе перамог! Будзь смелым, шчырым да сябе і прыпыні вярзці лухту!!! Усе ведаюць, што я моцны бліц-гулец, я магу перамагчы ўсіх у свеце за адну гульню! І "у"эслі "с"о — гэта нiхто для мяне, проста гулец, што плача кожны раз, калі прайграе, ( успомні, што ты казаў пра Фіруджа ) !!! Годзе гуляцца з маім імем, я заслугоўваю мець добрую рэпутацыю ва ўсёй шахматнай кар’еры, я афіцвйна запрашаю цябе на бліц матч ужывую з прызавым фондам! Мы абое паставім 5000$ і пераможца забярэ іх усіх! Прапаную ўсім іншым зацікаўленым паглядзець на мае рэзультаты ў 2016 і 2017 на бліц чэпміянаце свету і гэтага будзе дастаткова... Не варта слухаць кожнае ныццё, Тыгран Петрасян заўсёды гуляе сумленна! І калі нехта працягне пра мяне гэтак казаць, мы сустрэнемся ў судзе! Хай жыве ісціна! Ісціна не памрэ! А хлусаў выганяць...
'''
KEYWORDS = ["піпі", "памперс", "тыгран", "петрасян"]

bot = telebot.TeleBot(BOT_TOKEN)

last_processed_messages = {} # chat_id : last_message_id

@bot.message_handler(func=lambda message: True)
def handle_new_messages(message):
    if not message.text:
        return
    
    chat_id = message.chat.id
    if chat_id not in last_processed_messages or message.message_id > last_processed_messages[chat_id]:

        text = message.text.lower()
        found_keywords = [word for word in KEYWORDS if word in text]

        if (found_keywords):
            try:
                print('replying')
                bot.reply_to(message, COPYPASTA)
            except Exception as e:
                print(f"Error reacting to message: {e}")


if __name__ == "__main__":
    print('bot is running')
    bot.infinity_polling()