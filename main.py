import telebot
from telebot import types

# Создание бота
bot = telebot.TeleBot('5282614932:AAHCKYExnxxCg-CaiQFDmuu9HThvcPVZT8s')


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
    bot.send_message(m.chat.id,
                     'Привет! '
                     '\nНажми: '
                     '\nЧто рядом? — ближайшие к тебе места в парке, и викторины по пути '
                     '\nПрирода парка — про растения и животные парка '
                     '\nИнформация — полная карта парка, о команде проекта',
                     reply_markup=markup)


@bot.message_handler(commands=["test"])
def test(m):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    main = types.KeyboardButton("Главная")
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    markup.add(button_geo, main)
    bot.send_message(m.chat.id,
                     'Отправьте, пожалуйста, свое местоположение, нажав на кнопку',
                     reply_markup=markup)


# @bot.message_handler(content_types=["location"])
# def location_test(message):
#     if message.location is not None:
#         print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
#         print("Success")
#         # bot.send_message(message.chat.id, "Пока вы идете к точке, предлагаем вам пройти викторину, введя слово "
#         #                                   "викторина")


@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
        if 56.8927491 < message.location.latitude < 56.9194889 and 60.6480312 < message.location.longitude < 60.6844703:
            print("Success")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Что рядом?")
            item2 = types.KeyboardButton("Природа парка")
            item4 = types.KeyboardButton("Доп.Информация")
            markup.add(item1, item2)
            markup.add(item4)
            # bot.send_message(message.chat.id, "Пока вы идете к точке, предлагаем вам пройти викторину, введя слово "
            #                                   "викторина")

        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Что рядом?")
            item2 = types.KeyboardButton("Природа парка")
            item4 = types.KeyboardButton("Доп.Информация")
            markup.add(item1, item2)
            markup.add(item4)
            print("Fail")
            bot.send_message(message.chat.id, "К сожалению, ты находишься вне парка, приходи в парк чтобы "
                                              "использовать эту функцию", reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
# Ответы и сообщения
def handle_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, "Привет!")

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
        bot.send_message(message.chat.id, "Если вы тестируете геолокацию введите /test, "
                                          "чтобы перейти в тестовый режим")

    # elif message.text.lower() == 'викторина':
    #     bot.send_message(message.chat.id, "В разработке!")

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

    elif message.text.lower() == 'сосна':
        bot.send_message(message.chat.id, "Одно из популярнейших деревьев на территории России. Вечнозеленое, "
                                          "однодомное растение, произрастающее во многих азиатских и европейских "
                                          "регионах. Деревья этого вида вызывают повышенный интерес не только со "
                                          "стороны ботаников, но и у ландшафтных дизайнеров. Сосны становятся "
                                          "украшением парков, дворов и скверов.")

    elif message.text.lower() == 'клевер':
        bot.send_message(message.chat.id, "Латинское название рода происходит от tres — «три» и folium — «лист», "
                                          "дословно означая «трилистник». Русское название, впервые встречающееся в "
                                          "Травнике Николая Любчанина (1534), было заимствовано в XVI веке из "
                                          "немецкого языка. Некоторые виды клевера также называют «кашкой». "
                                          "Однолетние, "
                                          "двулетние и многолетние травы небольших или средних размеров. Листья в "
                                          "основном тройчатые, реже пятерные")

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
