import telebot
from extensions import *  # импортируем все классы из файла extensions.py
from config import TOKEN  # импортируе токен из файла config.py


bot = telebot.TeleBot(TOKEN)  # проходим регистрацию бота в телеграмм


@bot.message_handler(commands=['start', 'help'])  # обрабочик команд для получения инструкций в телеграмм
def helper(message: telebot.types.Message):
    text = f'Чтобы начать работу введите команду боту в следующем формате через пробел: \n' \
           f'|имя валюты| |в какую валюту перевести| |количество переводимой валюты|\n' \
           f'Например: доллар рубль 40 \n' \
           f'Список доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])  # обработчик команды получения списка доступных валют
def values(message: telebot.types.Message):
    text = f'Доступные валюты:'
    for money in key.keys():
        text = '\n'.join((text, money))
    bot.reply_to(message, text)  # выводим ответ на команду в виде списка доступных валют


@bot.message_handler(content_types=['text'])  # обработчик текстовых сообщений телеграм
def converter(message: telebot.types.Message):
    try:
        value = message.text.split(' ')  # преобразуем введеный текст в список разбитый по пробелам
        ErrorsInput.errors_input(value)  # проверяем на избыток/недостаток аргументов на вводе extensions стр. 10, 13
        quote, base, amount = list(map(str.title, value))  # следим за регистром введенных аргументов
        ErrorsOutput.errors_output(quote, base, amount)  # проверяе корректность ввода extensions стр. 19, 21
        text = GetPrice.get_price(quote, base, amount)  # получаем готовый ответ на запрос extensions стр. 38, 40
        bot.send_message(message.chat.id, text)  # выводим полученный ответ в сообщение телеграм бота
    except ConvertionExecption as e:  # выводим допущенные ошибки при вводе пользователя в сообщение чата
        bot.reply_to(message, f'Ошибка пользователя! \n {e}')
    except Exception as e:  # выводим прочие ошибка в сообщение чата
        bot.reply_to(message, f'Не удалось обработать команду\n {e}')


if __name__ == "__main__":  # точка запуска программы
    bot.polling()
