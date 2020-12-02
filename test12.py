import telebot
import config
import datetime
from telebot import types
from sm import Game

f = open("Klyuchi.txt", encoding='utf-8')
bot = telebot.TeleBot(config.TOKEN)
comands_bot = ('/start ' '/info' '/!')
check_name = True
r_id = '847154448'
m_id = '681309508'
a_id = '382941071'
#time
mess={}                #Тут будем считать сообщения через словарь
mess_time = datetime.date.today()   #Храним сегодняшнюю дату
def qty_mess(qty):     #Функция для изменения кол-ва сообщений у пользователя
    itog = qty + 1
    return itog



@bot.message_handler(commands=['start'])  # ответ на команду старт
def welcome(message):
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот для регистрации тайных сант. Для начала советую перейти тебе  сюда /info для просмотра более подробной информации.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html')



@bot.message_handler(commands=['info'])
def send_info(message):
    bot.send_message(message.chat.id, '')


f =[ 847154448, 681309508]
@bot.message_handler(commands=['!'])
def chat(message):
    user_ch = message.text
    user_id = message.from_user.id 
    if user_id == f[0]:
        bot.send_message(f[1], message.text[2:] )
    elif user_id == f[1]:
        bot.send_message(f[0], message.text[2:])





@bot.message_handler(content_types=['text'])
def send_text(message):
    global mess
    global mess_time
    text = message.text
    ex = Game()
    bot_text = ex.sec_main(text)
    if mess_time != datetime.date.today(): #Если дата не 2020 12 30, сбрасываем все сообщения
        mess = {}
    if message.from_user.id not in mess: #Если пользователь не писал сообщения, то добавляем его ID в словарь и присваиваем 0 сообщений
        mess[message.from_user.id] = 0
    if mess[message.from_user.id] == 1: #Ставим ограничения на кол-во сообщений
        bot.send_message(message.from_user.id, 'Твой лимит исчерпан!\nПопробуй '+ str(datetime.date.today() + datetime.timedelta(days=30)))
    else:
        mess[message.from_user.id] = qty_mess(mess[message.from_user.id])
        bot.send_message(message.chat.id, bot_text)
        




bot.polling(none_stop=True)
