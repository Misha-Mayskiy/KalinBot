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
    item3 = types.KeyboardButton("Факты")
    item4 = types.KeyboardButton("Информация")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    # стартовое сообщение
    bot.send_message(m.chat.id,
                     'Привет! '
                     '\nНажми: '
                     '\nЧто рядом? — ближайшие к тебе места в парке, и викторины по пути '
                     '\nПрирода парка — про растения и животные парка '
                     '\nФакты — о парке, интересные и развивающие '
                     '\nИнформация — полная карта парка, о команде проекта',
                     reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
# Ответы и сообщения
def handle_text(message):
    if message.text.strip() == 'Привет':
        answer = "Привет!"

    elif message.text.strip() == 'Пока':
        answer = "Ждем вас в лесопарке Калиновский!"

    elif message.text.strip() == 'Что рядом?':
        answer = "В разработке!"

    elif message.text.strip() == 'Природа парка':
        answer = "В разработке!"

    elif message.text.strip() == 'Викторины, факты':
        answer = "В разработке!"

    elif message.text.strip() == 'Информация':
        answer = "Наша команда: " \
                 "\nБатурин Михаил " \
                 "\nОлег Гельруд " \
                 "\nМихаил Пятых " \
                 "\nМария Кузнецова " \
                 "\nСергей Григорян " \
                 "\nКарту вы также можете посмотреть по ссылке: " \
                 "\nhttps://goo.su/JGnb"
        bot.send_photo(message.chat.id, 'https://ia.wampi.ru/2022/05/12/map.png')
    else:
        answer = "Прости, я не понял тебя :("

    bot.send_message(message.chat.id, answer, disable_web_page_preview=True)


# Запуск бота
bot.polling(none_stop=True, interval=0)
