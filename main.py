import telebot
from telebot import types

# Создание бота
bot = telebot.TeleBot('5282614932:AAHCKYExnxxCg-CaiQFDmuu9HThvcPVZT8s')
map_eco = "Карта эко-маршрута", 56.8937086, 60.6518539
vstrechi = "Место для встреч", 56.8947213, 60.6533790
rodniki = "Родники \"Бодрость\" и \"Лень\"", 56.8955355, 60.6530547
polyana = "Большая игровая поляна", 56.8978818, 60.6544989
vyshka = "Старая вышка", 56.8977055, 60.6539172
polyana2 = "Большая поляна", 56.9003373, 60.6548521


global answer
global count_places
global place
global find


# /start, /help
@bot.message_handler(commands=["start", "help"])
def start(m):
    # Добавление кнопок
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Что рядом? 🗺")
    item2 = types.KeyboardButton("Природа парка 🌲")
    item4 = types.KeyboardButton("Доп.Информация❓")
    markup.add(item1, item2)
    markup.add(item4)
    # стартовое сообщение
    print(m.chat.id)
    bot.send_message(m.chat.id,
                     'Привет! '
                     '\nНажми: '
                     '\nЧто рядом? — ближайшие к тебе места в парке, и викторины по пути '
                     '\nПрирода парка — про растения и животные парка '
                     '\nДоп.Информация — полная карта парка и другое',
                     reply_markup=markup)


@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))

        if 56.8927491 < message.location.latitude < 56.9194889 \
                and 60.6480312 < message.location.longitude < 60.6844703:
            find = False
            place = []
            count_places = 0
            print("Success")

            if 56.8945355 < message.location.latitude < 56.8965355 \
                    and 60.6520547 < message.location.longitude < 60.6540547:
                place += rodniki
                find = True
                count_places += 1

            if 56.8967055 < message.location.latitude < 56.8987055 \
                    and 60.6529172 < message.location.longitude < 60.6549172:
                place += vyshka
                find = True
                count_places += 1

            if 56.8993373 < message.location.latitude < 56.9013373 \
                    and 60.6538521 < message.location.longitude < 60.6558521:
                place += polyana2
                find = True
                count_places += 1

            if 56.8937213 < message.location.latitude < 56.8957213 \
                    and 60.6523790 < message.location.longitude < 60.6543790:
                place += vstrechi
                find = True
                count_places += 1

            if 56.8968818 < message.location.latitude < 56.8988818 \
                    and 60.6534989 < message.location.longitude < 60.6554989:
                place += polyana
                find = True
                count_places += 1

            if 56.8927086 < message.location.latitude < 56.8947086 \
                    and 60.6508539 < message.location.longitude < 60.6528539:
                place += map_eco
                find = True
                count_places += 1

            if find and count_places == 1:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                questions = types.KeyboardButton("Викторина")
                main = types.KeyboardButton("Главная")
                geolocation = types.KeyboardButton("Отправить местоположение ещё раз", request_location=True)
                markup.add(geolocation)
                markup.add(questions, main)

                bot.send_location(message.from_user.id, place[1], place[2])
                bot.send_message(message.chat.id, (
                        'Спасибо что посетили парк, найдено ближайшее к вам место: \n"' + place[0] + "\""),
                                 reply_markup=markup)
                bot.send_message(message.chat.id, "Пока вы идете к точке, предлагаем пройти викторину, "
                                                  "нажав по кнопке в нижней панели")

            if find and count_places >= 2:
                print("Finded places:", place[0], place[3])

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                questions = types.KeyboardButton("Викторина")
                main = types.KeyboardButton("Главная")
                geolocation = types.KeyboardButton("Отправить местоположение ещё раз", request_location=True)
                markup.add(geolocation)
                markup.add(questions, main)
                bot.send_location(message.from_user.id, place[1], place[2])
                bot.send_message(message.chat.id, (
                        'Спасибо что посетили парк, найдены ближайшие к вам места: \n' + place[0] + "\n" + place[3]))
                bot.send_location(message.from_user.id, place[4], place[5])

                bot.send_message(message.chat.id, "Пока вы идете к точке, предлагаем вам пройти викторину, "
                                                  "нажав по кнопке в нижней панели", reply_markup=markup)

            if not find:

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                questions = types.KeyboardButton("Викторина")
                main = types.KeyboardButton("Главная")
                geolocation = types.KeyboardButton("Отправить местоположение ещё раз", request_location=True)
                markup.add(geolocation)
                markup.add(questions, main)

                bot.send_message(message.chat.id, "К сожалению, в 100 метрах от вас ничего не найдено, "
                                                  "вы можете идти дальше по маршруту и отправлять геолокацию,"
                                                  " а также пройти развлекательную викторину",
                                 reply_markup=markup)

        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Что рядом? 🗺")
            item2 = types.KeyboardButton("Природа парка 🌲")
            item4 = types.KeyboardButton("Доп.Информация❓")
            markup.add(item1, item2)
            markup.add(item4)
            print("Fail")
            bot.send_message(message.chat.id, "К сожалению, ты находишься вне парка, приходи в парк чтобы "
                                              "использовать эту функцию", reply_markup=markup)


# Получение сообщений от юзера и ответ бота на него
@bot.message_handler(content_types=["text"])
def handle_text(message):
    print(message.from_user.first_name, message.from_user.last_name, message.from_user.username, ":", message.text)

    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, ("Привет," + message.from_user.first_name + "!"))

    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, "Ждем вас в лесопарке Калиновский!")

    elif message.text.lower() == 'главная':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Что рядом? 🗺")
        item2 = types.KeyboardButton("Природа парка 🌲")
        item3 = types.KeyboardButton("Доп.Информация❓")
        markup.add(item1, item2)
        markup.add(item3)
        bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=markup)
    elif message.text.lower() == 'что рядом? 🗺':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        main = types.KeyboardButton("Главная")
        button_geo = types.KeyboardButton(text="Отправить местоположение 🌍", request_location=True)
        markup.add(button_geo, main)
        bot.send_message(message.chat.id,
                         'Отправьте, пожалуйста, свое местоположение, нажав на кнопку',
                         reply_markup=markup)

    elif message.text.lower() == 'викторина':
        global n
        n = 0
        bot.send_message(message.chat.id, "Развлекательная викторина начинается!")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("Завод")
        # Correct
        a2 = types.KeyboardButton("Золотодобыча")
        a3 = types.KeyboardButton("Рыболовство")
        a4 = types.KeyboardButton("Охотничьи угодья")
        markup.add(a1, a2)
        markup.add(a3, a4)

        bot.send_message(message.chat.id, 'Что раньше было на территории лесного парка?',
                         reply_markup=markup)

    elif message.text.lower() == "завод":
        bot.send_message(message.chat.id, 'Неверно, правильный ответ был: Золотодобыча')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("Баба Яга")
        a2 = types.KeyboardButton("Леший")
        a3 = types.KeyboardButton("Лесничий")
        a4 = types.KeyboardButton("Змей Горыныч")
        markup.add(a1, a2)
        markup.add(a3, a4)

        bot.send_message(message.chat.id, 'Кордоны всегда строят в лесных парках. Как ты думаешь, кто в них живёт?',
                         reply_markup=markup)

    elif message.text.lower() == 'золотодобыча':
        n += 1
        bot.send_message(message.chat.id, 'Верно, +1 балл!')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("Баба Яга")
        a2 = types.KeyboardButton("Леший")
        a3 = types.KeyboardButton("Лесничий")
        a4 = types.KeyboardButton("Змей Горыныч")
        markup.add(a1, a2)
        markup.add(a3, a4)

        bot.send_message(message.chat.id, 'Кордоны всегда строят в лесных парках. Как ты думаешь, кто в них живёт?',
                         reply_markup=markup)

    elif message.text.lower() == "рыболовство":
        bot.send_message(message.chat.id, 'Неверно, правильный ответ был: Золотодобыча')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("Баба Яга")
        a2 = types.KeyboardButton("Леший")
        a3 = types.KeyboardButton("Лесничий")
        a4 = types.KeyboardButton("Змей Горыныч")
        markup.add(a1, a2)
        markup.add(a3, a4)

        bot.send_message(message.chat.id, 'Кордоны всегда строят в лесных парках. Как ты думаешь, кто в них живёт?',
                         reply_markup=markup)

    elif message.text.lower() == "охотничьи угодья":
        bot.send_message(message.chat.id, 'Неверно, правильный ответ был: Золотодобыча')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("Баба Яга")
        a2 = types.KeyboardButton("Леший")
        a3 = types.KeyboardButton("Лесничий")
        a4 = types.KeyboardButton("Змей Горыныч")
        markup.add(a1, a2)
        markup.add(a3, a4)

        bot.send_message(message.chat.id, 'Кордоны всегда строят в лесных парках. Как ты думаешь, кто в них живёт?',
                         reply_markup=markup)

    elif message.text.lower() == "баба яга":
        bot.send_message(message.chat.id, 'Неверно, правильный ответ был: Лесничий')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("Затопило шахты")
        a2 = types.KeyboardButton("Упал метеорит")
        a3 = types.KeyboardButton("Были там всегда")
        a4 = types.KeyboardButton("Специально созданы")
        markup.add(a1, a2)
        markup.add(a3, a4)

        bot.send_message(message.chat.id, 'Как образовались водоёмы?',
                         reply_markup=markup)

    elif message.text.lower() == "леший":
        bot.send_message(message.chat.id, 'Неверно, правильный ответ был: Лесничий')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("Затопило шахты")
        a2 = types.KeyboardButton("Упал метеорит")
        a3 = types.KeyboardButton("Были там всегда")
        a4 = types.KeyboardButton("Специально созданы")
        markup.add(a1, a2)
        markup.add(a3, a4)

        bot.send_message(message.chat.id, 'Как образовались водоёмы?',
                         reply_markup=markup)

    elif message.text.lower() == "лесничий":
        n += 1
        bot.send_message(message.chat.id, 'Верно, +1 балл!')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("Затопило шахты")
        a2 = types.KeyboardButton("Упал метеорит")
        a3 = types.KeyboardButton("Были там всегда")
        a4 = types.KeyboardButton("Специально созданы")
        markup.add(a1, a2)
        markup.add(a3, a4)

        bot.send_message(message.chat.id, 'Как образовались водоёмы?',
                         reply_markup=markup)

    elif message.text.lower() == "змей горыныч":
        bot.send_message(message.chat.id, 'Неверно, правильный ответ был: Лесничий')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("Затопило шахты")
        a2 = types.KeyboardButton("Упал метеорит")
        a3 = types.KeyboardButton("Были там всегда")
        a4 = types.KeyboardButton("Специально созданы")
        markup.add(a1, a2)
        markup.add(a3, a4)

        bot.send_message(message.chat.id, 'Как образовались водоёмы?',
                         reply_markup=markup)

    elif message.text.lower() == "змей горыныч":
        bot.send_message(message.chat.id, 'Неверно, правильный ответ был: Лесничий')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("Затопило шахты")
        a2 = types.KeyboardButton("Упал метеорит")
        a3 = types.KeyboardButton("Были там всегда")
        a4 = types.KeyboardButton("Специально созданы")
        markup.add(a1, a2)
        markup.add(a3, a4)

        bot.send_message(message.chat.id, 'Как образовались водоёмы?',
                         reply_markup=markup)

    elif message.text.lower() == "упал метеорит":
        bot.send_message(message.chat.id, 'Неверно, правильный ответ был: Затопило шахты')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("Русские")
        a2 = types.KeyboardButton("Башкиры")
        a3 = types.KeyboardButton("Украинцы")
        a4 = types.KeyboardButton("Татары")
        markup.add(a1, a2)
        markup.add(a3, a4)

        bot.send_message(message.chat.id, 'Как ты думаешь, какой народ традиционно проживает в хуторах?',
                         reply_markup=markup)

    elif message.text.lower() == "были там всегда":
        bot.send_message(message.chat.id, 'Неверно, правильный ответ был: Затопило шахты')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("Русские")
        a2 = types.KeyboardButton("Башкиры")
        a3 = types.KeyboardButton("Украинцы")
        a4 = types.KeyboardButton("Татары")
        markup.add(a1, a2)
        markup.add(a3, a4)

        bot.send_message(message.chat.id, 'Как ты думаешь, какой народ традиционно проживает в хуторах?',
                         reply_markup=markup)

    elif message.text.lower() == "специально созданы":
        bot.send_message(message.chat.id, 'Неверно, правильный ответ был: Затопило шахты')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("Русские")
        a2 = types.KeyboardButton("Башкиры")
        a3 = types.KeyboardButton("Украинцы")
        a4 = types.KeyboardButton("Татары")
        markup.add(a1, a2)
        markup.add(a3, a4)

        bot.send_message(message.chat.id, 'Как ты думаешь, какой народ традиционно проживает в хуторах?',
                         reply_markup=markup)

    elif message.text.lower() == "затопило шахты":
        n += 1
        bot.send_message(message.chat.id, 'Верно, +1 балл!')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("Русские")
        a2 = types.KeyboardButton("Башкиры")
        a3 = types.KeyboardButton("Украинцы")
        a4 = types.KeyboardButton("Татары")
        markup.add(a1, a2)
        markup.add(a3, a4)

        bot.send_message(message.chat.id, 'Как ты думаешь, какой народ традиционно проживает в хуторах?',
                         reply_markup=markup)

    elif message.text.lower() == "русские":
        bot.send_message(message.chat.id, 'Неверно, правильный ответ был: Украинцы')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("600-800")
        a2 = types.KeyboardButton("800-1000")
        a3 = types.KeyboardButton("1000-1200")
        a4 = types.KeyboardButton("1200-1400")
        markup.add(a1, a2)
        markup.add(a3, a4)

        bot.send_message(message.chat.id, 'Как ты думаешь, сколько гектаров занимает Калиновский лесной парк?',
                         reply_markup=markup)

    elif message.text.lower() == "башкиры":
        bot.send_message(message.chat.id, 'Неверно, правильный ответ был: Украинцы')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("600-800")
        a2 = types.KeyboardButton("800-1000")
        a3 = types.KeyboardButton("1000-1200")
        a4 = types.KeyboardButton("1200-1400")
        markup.add(a1, a2)
        markup.add(a3, a4)

        bot.send_message(message.chat.id, 'Как ты думаешь, сколько гектаров занимает Калиновский лесной парк?',
                         reply_markup=markup)

    elif message.text.lower() == "татары":
        bot.send_message(message.chat.id, 'Неверно, правильный ответ был: Украинцы')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("600-800")
        a2 = types.KeyboardButton("800-1000")
        a3 = types.KeyboardButton("1000-1200")
        a4 = types.KeyboardButton("1200-1400")
        markup.add(a1, a2)
        markup.add(a3, a4)

        bot.send_message(message.chat.id, 'Как ты думаешь, сколько гектаров занимает Калиновский лесной парк?',
                         reply_markup=markup)

    elif message.text.lower() == "украинцы":
        n += 1
        bot.send_message(message.chat.id, 'Верно, +1 балл!')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("600-800")
        a2 = types.KeyboardButton("800-1000")
        a3 = types.KeyboardButton("1000-1200")
        a4 = types.KeyboardButton("1200-1400")
        markup.add(a1, a2)
        markup.add(a3, a4)

        bot.send_message(message.chat.id, 'Как ты думаешь, сколько гектаров занимает Калиновский лесной парк?',
                         reply_markup=markup)

    elif message.text.lower() == "600-800":
        bot.send_message(message.chat.id, 'Неверно, правильный ответ был: 1000-1200')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("Главная")
        a2 = types.KeyboardButton("Отправить местоположение", request_location=True)
        markup.add(a2)
        markup.add(a1)
        bot.send_message(message.chat.id, ('Поздравляю! Ты прошел викторину на ' + str(n) + " баллов из 5!"),
                         reply_markup=markup)

    elif message.text.lower() == "1000-1200":
        n += 1
        bot.send_message(message.chat.id, 'Верно, +1 балл!')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("Главная")
        a2 = types.KeyboardButton("Отправить местоположение", request_location=True)
        markup.add(a2)
        markup.add(a1)
        bot.send_message(message.chat.id, ('Поздравляю! Ты прошел викторину на ' + str(n) + " баллов из 5!"),
                         reply_markup=markup)

    elif message.text.lower() == "1200-1400":
        bot.send_message(message.chat.id, 'Неверно, правильный ответ был: 1000-1200')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("Главная")
        a2 = types.KeyboardButton("Отправить местоположение", request_location=True)
        markup.add(a2)
        markup.add(a1)
        bot.send_message(message.chat.id, ('Поздравляю! Ты прошел викторину на ' + str(n) + " баллов из 5!"),
                         reply_markup=markup)

    elif message.text.lower() == "800-1000":
        bot.send_message(message.chat.id, 'Неверно, правильный ответ был: 1000-1200')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        a1 = types.KeyboardButton("Главная")
        a2 = types.KeyboardButton("Отправить местоположение", request_location=True)
        markup.add(a2)
        markup.add(a1)
        bot.send_message(message.chat.id, ('Поздравляю! Ты прошел викторину на ' + str(n) + " баллов из 5!"),
                         reply_markup=markup)

    elif message.text.lower() == 'доп.информация❓':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Карта 🗺")
        item2 = types.KeyboardButton("О проекте")
        item3 = types.KeyboardButton("Главная")
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Карта и о проекте", reply_markup=markup)

    elif message.text.lower() == 'карта 🗺':
        markup = types.InlineKeyboardMarkup()
        bot.send_photo(message.chat.id, 'https://ia.wampi.ru/2022/05/12/map.png')
        map_link = types.InlineKeyboardButton("Карта лесопарка", url='https://goo.gl/maps/a6SsEvY4XpgWAuZu9')
        markup.add(map_link)
        answer = "Также карту можно посмотреть по ссылке ниже"
        bot.send_message(message.chat.id, answer, reply_markup=markup)

    elif message.text.lower() == 'о проекте':
        answer = "\nВсе функции бота будут дополняться." \
                 "\nБот создан с целью заинтересовать и помочь посетителям лесного парка Калиновский."

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1, item2 = types.KeyboardButton("Команда проекта"), types.KeyboardButton("Главная")
        markup.add(item1, item2)

        bot.send_message(message.chat.id, answer, reply_markup=markup)

    elif message.text.lower() == 'команда проекта':
        answer = "\nКоманда проекта: " \
                 "\nБатурин Михаил - разработчик" \
                 "\nОлег Гельруд - контент-мейкер" \
                 "\nСергей Григорян - по викторинам"

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Главная"))
        bot.send_message(message.chat.id, answer, reply_markup=markup)

    elif message.text.lower() == 'природа парка 🌲':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        dyatel = types.KeyboardButton("Дятел")
        belka = types.KeyboardButton("Белка")
        kolokol = types.KeyboardButton("Колокольчик")
        sosna = types.KeyboardButton("Сосна")
        bereza = types.KeyboardButton("Береза")
        mim = types.KeyboardButton("Мать-и-мачеха")
        main = types.KeyboardButton("Главная")
        markup.add(mim, kolokol)
        markup.add(dyatel, belka)
        markup.add(sosna, bereza)
        markup.add(main)
        bot.send_message(message.chat.id,
                         text="Нажмите на кнопку в нижней панели, чтобы посмтреть информацию о растении или животном",
                         reply_markup=markup)

    elif message.text.lower() == 'дятел':
        bot.send_photo(message.chat.id, open('images/dyatel.jpg', 'rb'))
        bot.send_message(message.chat.id, "Очень красивая, легкоузнаваемая птица. Единственная птица, использующая "
                                          "для выражения чувств «музыкальные инструменты», роль которых играют сухие "
                                          "деревья. Сучья резонируют, что выливается в характерную трель — "
                                          "«механическую песню». Своеобразные постукивания дятлы используют и как "
                                          "средство связи, заявляя о своем владении территорией.")

    elif message.text.lower() == 'белка':
        bot.send_photo(message.chat.id, open('images/belocka.jpg', 'rb'))
        bot.send_message(message.chat.id, "Хлопотливый, шустрый и веселый зверек. Шерстка у белки густая и пушистая. "
                                          "Тельце маленькое, кругленькое, а хвост длинный и пушистый. Мордочка "
                                          "красивая, а ушки стоят торчком. Белочка питается желудями, орехами, "
                                          "личинками и грибами.")

    elif message.text.lower() == 'колокольчик':
        bot.send_photo(message.chat.id, open('images/kolokol.jpg', 'rb'))
        bot.send_message(message.chat.id, "Колокольчик красивое растение. Его цветок окрашен во все оттенки синего "
                                          "цвета. По своей форме колокольчик похож на настоящий колокол. У "
                                          "него тонкий и раскидистый стебель. Лепестки колокольчика образуют "
                                          "колоколообразную чашу.")

    elif message.text.lower() == 'мать-и-мачеха':
        bot.send_photo(message.chat.id, open('images/mim.jpg', 'rb'))
        bot.send_message(message.chat.id, "Внешне он напоминает одуванчик, но мать-и-мачеха меньше и всегда растет "
                                          "кучками. Листья мать-и-мачехи с верхней стороны гладкие и прохладные, "
                                          "а с нижней – бархатистые и теплые. Именно эта особенность дала цветку "
                                          "название. Теплая бархатная сторона сравнивается мамой, а холодная с "
                                          "мачехой.")

    elif message.text.lower() == 'сосна':
        bot.send_photo(message.chat.id, open('images/sosna.png', 'rb'))
        bot.send_message(message.chat.id, "Растет даже на песке, у неё сильные и глубокие корни благодаря "
                                          "которым сосна получает из глубины воду и питательные вещества. Из него "
                                          "опадают веточки и хвоя, которые образовывают плодородный грунт, "
                                          "где потом растут другие растения, грибы. Свои семена, которые содержатся в "
                                          "шишках, она дарит белочкам и птицам, которые живут в лесу.")

    elif message.text.lower() == 'береза':
        bot.send_photo(message.chat.id, open('images/bereza.jpg', 'rb'))
        bot.send_message(message.chat.id, "Белая красавица, дерево которое первым делом ассоциируется когда говорят "
                                          "об урале. Многие люди считают необходимым попробовать берёзовый сок, "
                                          "но совершенно забывают о том что подомными "
                                          "действиями наносят непоправимый урон дереву, которое в итоге погибает.")

    else:
        bot.send_message(message.chat.id, "Прости, я не понял тебя :(")


# @bot.callback_query_handler(func=lambda call: True)
# def answer(call):
#     if call.data == 'back':
#         bot.send_message(call.chat.id, "Вы вернулись назад", reply_markup=None)


# Запуск бота
bot.polling(none_stop=True, interval=1)
