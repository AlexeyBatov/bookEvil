import telebot
import datetime
from datetime import date
import calendar
my_date = date.today()
print(datetime.date.today(), calendar.day_name[my_date.weekday()], "hello, I'm bot")
bot = telebot.TeleBot('1077083517:AAGuxYmPPu8RVX534JP2WC-q3SjwE3MWolU')
dnv = ['/monday', '/tuesday', '/wednesday', '/thursday', '/friday']

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, это рассписание для 11 кл. Пиши /dnevnik. будут вопросы - /help. Сегодня:")
        bot.send_message(message.from_user.id, datetime.date.today())
        bot.send_message(message.from_user.id, calendar.day_name[my_date.weekday()])
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Вообщем: пишешь боту '/dnevnik' и выбераешь нужный день. В дальнейшем будут обновления, По вопросам к @Samo1lov")
    elif message.text == "/monday":
        bot.send_message(message.from_user.id, "Понедельник: И*/Х*, Англ.яз, Алгебра, Биология, Общество, Литература,Физика")
    elif message.text == "/tuesday":
        bot.send_message(message.from_user.id, "Физика, Экономика, Англ.яз, И/Х, Русский яз, История, физ-ра")
    elif message.text == "/wednesday":
        bot.send_message(message.from_user.id, "Физика, Литература, И*/Х*, Геометрия, Англ.яз, Математика, Физкультура")
    elif message.text == "/thursday":
        bot.send_message(message.from_user.id, "Физика, общество, Русский яз, История, Алгебра, ОБЖ, И*")
    elif message.text == "/friday":
        bot.send_message(message.from_user.id, "Геометрия, Физ-ра, И*/Х*, Физика, Литература, Алгебра")
    elif message.text == "/dnevnik":
        bot.send_message(message.chat.id, '\n'.join(dnv))
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю напиши /help")

bot.polling(none_stop=True, interval=0)