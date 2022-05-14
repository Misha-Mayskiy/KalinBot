import telebot
from telebot import types

# Создание бота
bot = telebot.TeleBot('5282614932:AAHCKYExnxxCg-CaiQFDmuu9HThvcPVZT8s')
place = "небольшое озерцо с живописными берегами"

# /start
@bot.message_handler(commands=["start"])
def start(m):
    # Добавление кнопок
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Что рядом?")
    item2 = types.KeyboardButton("Природа парка")
    item4 = types.KeyboardButton("Доп.Информация")
    markup.add(item1, item2)
    markup.add(item4)
    # стартовое сообщение
    print(m.chat.id)
    bot.send_message(m.chat.id,
                     'Привет! '
                     '\nНажми: '
                     '\nЧто рядом? — ближайшие к тебе места в парке, и викторины по пути '
                     '\nПрирода парка — про растения и животные парка '
                     '\nИнформация — полная карта парка, о команде проекта',
                     reply_markup=markup)


@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
        # if 56.8927491 < message.location.latitude < 56.9194889 and 60.6480312 < message.location.longitude < 60.6844703:
        print("Success")
        bot.send_message(message.chat.id, ("Спасибо что посетили парк, найдено ближайшее к вам место:", place))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Что рядом?")
        item2 = types.KeyboardButton("Природа парка")
        item4 = types.KeyboardButton("Доп.Информация")
        markup.add(item1, item2)
        markup.add(item4)
        bot.send_location(message.from_user.id, 56.910849, 60.651772)
        bot.send_message(message.chat.id, "Пока вы идете к точке, предлагаем вам пройти викторину, введя слово "
                                          "викторина", reply_markup=markup)


    # else:
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     item1 = types.KeyboardButton("Что рядом?")
    #     item2 = types.KeyboardButton("Природа парка")
    #     item4 = types.KeyboardButton("Доп.Информация")
    #     markup.add(item1, item2)
    #     markup.add(item4)
    #     print("Fail")
    #     bot.send_message(message.chat.id, "К сожалению, ты находишься вне парка, приходи в парк чтобы "
    #                                       "использовать эту функцию", reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
# Ответы и сообщения
def handle_text(message):
    print(message.from_user.first_name, message.from_user.last_name, message.from_user.username, ":", message.text)
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, ("Привет," + message.from_user.first_name +
                                           " " + message.from_user.last_name + "!"))

    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, "Ждем вас в лесопарке Калиновский!")

    elif message.text.lower() == 'что рядом?':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        main = types.KeyboardButton("Главная")
        button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
        markup.add(button_geo, main)
        bot.send_message(message.chat.id,
                         'Отправьте, пожалуйста, свое местоположение, нажав на кнопку',
                         reply_markup=markup)

    elif message.text.lower() == 'викторина':
        bot.send_message(message.chat.id, "Развлекательная викторина начинается!")
        for i in range(0, 6):
            if i == 1:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Четверть")
                item2 = types.KeyboardButton("Половину")
                item4 = types.KeyboardButton("Треть")
                item3 = types.KeyboardButton("Почти ничего")
                markup.add(item1, item2)
                markup.add(item4, item3)
                bot.send_message(message.chat.id, 'Как ты думаешь, какую часть суши занимают леса?',
                                 reply_markup=markup)

            if i == 2:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Вся бумага")
                item2 = types.KeyboardButton("Бумага не создается из мукулатуры")
                item4 = types.KeyboardButton("Треть")
                item3 = types.KeyboardButton("Половина всей бумаги")
                markup.add(item1, item2)
                markup.add(item4, item3)
                bot.send_message(message.chat.id, 'Как ты думаешь, сколько бумаги создаëтся и макулатуры?',
                                 reply_markup=markup)

            if i == 3:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Вся Финляндия")
                item2 = types.KeyboardButton("Половина")
                item4 = types.KeyboardButton("Две трети")
                item3 = types.KeyboardButton("Четверть")
                markup.add(item1, item2)
                markup.add(item4, item3)
                bot.send_message(message.chat.id, 'Финляндия самая лесистая страна Европы. Как ты думаешь, как много '
                                                  'територии Финляндии покрыто лесами?',
                                 reply_markup=markup)

            if i == 4:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("4 тонны")
                item2 = types.KeyboardButton("10 тонн")
                item4 = types.KeyboardButton("3 тонны")
                item3 = types.KeyboardButton("5 килограмм")
                markup.add(item1, item2)
                markup.add(item4, item3)
                bot.send_message(message.chat.id, 'Как ты думаешь, сколько бумаги получится из одного дерева?',
                                 reply_markup=markup)

            if i == 5:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Людей")
                item2 = types.KeyboardButton("Деревьев")
                item4 = types.KeyboardButton("И тех, и других одинаково много")
                item3 = types.KeyboardButton("Все деревья не возможно посчитать")
                markup.add(item1, item2)
                markup.add(item4, item3)
                bot.send_message(message.chat.id, 'В мире больше людей или деревьев?',
                                 reply_markup=markup)

    elif message.text.lower() == 'природа парка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        plants = types.KeyboardButton("Растения лесопарка")
        animals = types.KeyboardButton("Животные лесопарка")
        item2 = types.KeyboardButton("Главная")
        markup.add(plants)
        markup.add(animals)
        markup.add(item2)
        bot.send_message(message.chat.id,
                         text="Нажмите на кнопку, чтобы получить список растений или животных лесного парка",
                         reply_markup=markup)

    elif message.text.lower() == 'главная':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Что рядом?")
        item2 = types.KeyboardButton("Природа парка")
        item3 = types.KeyboardButton("Доп.Информация")
        markup.add(item1, item2)
        markup.add(item3)
        bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)

    elif message.text.lower() == 'доп.информация':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Карта")
        item2 = types.KeyboardButton("О проекте")
        item3 = types.KeyboardButton("Главная")
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Карта и о проекте", reply_markup=markup)

    elif message.text.lower() == 'карта':
        markup = types.InlineKeyboardMarkup()
        bot.send_photo(message.chat.id, 'https://ia.wampi.ru/2022/05/12/map.png')
        map_link = types.InlineKeyboardButton("Карта лесопарка", url='https://goo.gl/maps/a6SsEvY4XpgWAuZu9')
        markup.add(map_link)
        answer = "Также карту можно посмотреть по ссылке ниже"
        bot.send_message(message.chat.id, answer, reply_markup=markup)

    elif message.text.lower() == 'о проекте':
        answer = "\nВсе функции бота будут дополняться" \
                 "\nКоманда проекта: " \
                 "\nБатурин Михаил - разработчик" \
                 "\nОлег Гельруд - основатель команды" \
                 "\nСергей Григорян - викторины" \
                 "\nМария Кузнецова - природа парка" \
                 "\nМихаил Пятых"

        bot.send_message(message.chat.id, answer)

    else:
        bot.send_message(message.chat.id, "Прости, я не понял тебя :(")


# Запуск бота
bot.polling(none_stop=True)
