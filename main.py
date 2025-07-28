import telebot
from dotenv import load_dotenv
import os
import kdb

load_dotenv()

TOKEN = os.getenv('TELEGRAMbotTOKEN')
COPYPASTA = '''
Ты здзекуешся ??? Што за ***** ты вярзеш, чал ? Ты найбольшы няўдаха, якога я бачыў у жыцці ! Ты рабіў ПІПІ ў свае памперсы, пакуль я перамагаў гульцоў нашмат мацнейшых за цябе! Ты не прафесіянал, бо прафесіяналы ўмеюць прайграваць і віншаваць апанентаў, а ты як дзяўчынка, што плача пасля таго, як я цябе перамог! Будзь смелым, шчырым да сябе і прыпыні вярзці лухту!!! Усе ведаюць, што я моцны бліц-гулец, я магу перамагчы ўсіх у свеце за адну гульню! І "у"эслі "с"о — гэта нiхто для мяне, проста гулец, што плача кожны раз, калі прайграе, ( успомні, што ты казаў пра Фіруджа ) !!! Годзе гуляцца з маім імем, я заслугоўваю мець добрую рэпутацыю ва ўсёй шахматнай кар’еры, я афіцыйна запрашаю цябе на бліц матч ужывую з прызавым фондам! Мы абое паставім 5000$ і пераможца забярэ іх усіх! Прапаную ўсім іншым зацікаўленым паглядзець на мае рэзультаты ў 2016 і 2017 на бліц чэпміянаце свету і гэтага будзе дастаткова... Не варта слухаць кожнае ныццё, Тыгран Петрасян заўсёды гуляе сумленна! І калі нехта працягне пра мяне гэтак казаць, мы сустрэнемся ў судзе! Хай жыве ісціна! Ісціна не памрэ, а хлусы — так...
'''
KEYWORDS = ["піпі", "памперс", "тыгран", "петрасян"]

bot = telebot.TeleBot(TOKEN)

lastPROCESSEDmessages = {}

@bot.message_handler(func=lambda message: True)
def handle_new_messages(message):
    if not message.text:
        return
    
    chatID = message.chat.id
    if chatID not in lastPROCESSEDmessages or message.message_id > lastPROCESSEDmessages[chatID]:

        text = message.text.lower()
        foundKEYWORDS = [word for word in KEYWORDS if word in text]

        if foundKEYWORDS:
            try:
                if message.reply_to_message:
                    print('Replying to the original message')
                    bot.reply_to(message.reply_to_message, COPYPASTA)
                else:
                    print('No reply found, replying directly')
                    bot.reply_to(message, COPYPASTA)
                    
            except Exception as e:
                print(f"Error reacting to message: {e}")


if __name__ == "__main__":
    print('bot is running')
    bot.infinity_polling()