import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button1 = types.KeyboardButton('Проблемы с принтером')
    button2 = types.KeyboardButton('Проблемы с кассой')
    button3 = types.KeyboardButton('Проблемы с интернетом')
    markup.add(button1, button2, button3)
    sti = open('static/welcome.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы помогать вам.".format(message.from_user, bot.get_me()),
            parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['website'])
def open_problem(message):
    markup=types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://xn--80aale2ao9a2e.xn--p1ai/"))
    bot.send_message(message.chat.id, "Актуальныя информация на сайте, просто нажми на кнопку", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['id'])
def answer(message):
    print(message.chat.id)


# Функция для появления ошибок принтра
@bot.message_handler(content_types=['text'])
def question_printer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button1 = types.KeyboardButton('Зажевало бумагу')
    button2 = types.KeyboardButton('Не печатает с двух сторон')
    button3 = types.KeyboardButton('Не печатает')
    markup.add(button1, button2, button3)
    id=message.chat.id
    msg=message.text
    sti = open('static/RRR.tgs', 'rb')
    stic = open('static/FireRUN.tgs', 'rb')
    stice = open('static/FireNote.tgs', 'rb')
    sticer = open('static/FireZLO.tgs', 'rb')
    plak = open('static/Plak.tgs', 'rb')

    if msg == 'Проблемы с принтером':
        bot.send_message(message.chat.id, 'Подскажите какая проблема у вас с принтером?'.format(message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=markup)
    elif msg == 'Зажевало бумагу':
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://www.youtube.com/watch?v=huk4xA6fyP8&ab_channel=KYOCERAUAOfficeSystemLTD"))
        bot.send_message(message.chat.id, "Как достать бумагу из принтера? Просто нажмите на кнопку и посмотрите видео", parse_mode='html', reply_markup=markup)

    elif msg == 'Не печатает с двух сторон':
        bot.send_message(message.chat.id,"Инструкция")
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('photo_printer/1.jpg', 'rb')), telebot.types.InputMediaPhoto(open('photo_printer/2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('photo_printer/3.jpg', 'rb')),telebot.types.InputMediaPhoto(open('photo_printer/4.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('photo_printer/5.jpg', 'rb'))])
    elif msg == 'Не печатает':
        bot.send_message(message.chat.id,"Для начала не стоит паниковать.Проверьте, стоит ли ваш принтер в приоритете.Просто следуйте следующей инструкции:")
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('photo_printer/1.jpg', 'rb')), telebot.types.InputMediaPhoto(open('photo_printer/2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('photo_printer/3.jpg', 'rb')),telebot.types.InputMediaPhoto(open('photo_printer/6.jpg', 'rb'))])

    elif msg == 'Проблемы с кассой':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        button1 = types.KeyboardButton('Не печатает чек')
        button2 = types.KeyboardButton('Не открывает смену')
        markup.add(button1, button2)
        bot.send_message(message.chat.id, 'Подскажите какая проблема у вас с кассой?'.format(message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=markup)
    elif msg == 'Не печатает чек':
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(message.chat.id,"Инструкция:\n 1)Зажмите красную кнопку до отключения кассы\n 2)Переподключите провод интернета\n 3)Включите кассу зажатием зелёной кнопки")

        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('photo_printer/11.jpg', 'rb')), telebot.types.InputMediaPhoto(open('photo_printer/12.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('photo_printer/13.jpg', 'rb'))])
    elif msg == 'Не открывает смену':
        bot.send_sticker(message.chat.id, stic)
        bot.send_message(message.chat.id,"Инструкция:\n 1)Попробуйте воспользоваться самым верным способом и просто перезагрузите компьютер!\n 2)Не помогло? странно...Напишите системному администратору")

    elif msg == 'Проблемы с интернетом':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        button1 = types.KeyboardButton('Нет интернета')
        button2 = types.KeyboardButton('Виснет YouTube, Фильмы для детей')
        markup.add(button1, button2)
        bot.send_message(message.chat.id, 'Подскажите какая проблема у вас с интернетом?'.format(message.from_user, bot.get_me()),
                            parse_mode='html', reply_markup=markup)

    elif msg == 'Нет интернета':
        bot.send_sticker(message.chat.id, stice)
        bot.send_message(message.chat.id,"Инструкция:\n 1)Для начала не нужно паники, не спешите писать системному администратору, ведь чаще всего с данной проблемой выможете справиться самостоятельно\n2)Переподключите провод интернета в системном блоке")
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('photo_printer/16.jpg', 'rb')), telebot.types.InputMediaPhoto(open('photo_printer/17.jpg', 'rb'))])

    elif msg == 'Виснет YouTube, Фильмы для детей':
        bot.send_sticker(message.chat.id, sticer)
        bot.send_message(message.chat.id,"Инструкция:\n 1)Не переживайте, данная проблема тоже решается очень просто!\n2)Просто перезагрузите ваш браузер\n3) Если не помогло переподключите интернет провод")
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('photo_printer/16.jpg', 'rb')), telebot.types.InputMediaPhoto(open('photo_printer/17.jpg', 'rb'))])
# Функция для появления ошибок Кассы
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        button1 = types.KeyboardButton('Проблемы с принтером')
        button2 = types.KeyboardButton('Проблемы с кассой')
        button3 = types.KeyboardButton('Проблемы с интернетом')
        markup.add(button1, button2, button3)
        sti = open('static/welcome.tgs', 'rb')
        bot.send_sticker(message.chat.id, plak)

        bot.send_message(message.chat.id, "Я еще глуповат и не понимаю вас, напишите системеному администратору.".format(message.from_user, bot.get_me()),
                            parse_mode='html', reply_markup=markup)

bot.polling(none_stop=True, timeout=123)
