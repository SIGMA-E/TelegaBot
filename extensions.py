import requests
import json
from config import key  # импортируем словарь с доступными валютами из файла config.py


class ConvertionExecption(Exception):  # создаем пустой класс ошибок
    pass


class ErrorsInput:  # класс ошибок при избытке или недостатке аргументов на вводе
    @staticmethod  # декоратор позволяющий обращаться к методу класса напрямую файл TelegaBot_060223 строка 30
    def errors_input(value):  # передаем в функцию список из файла TelegaBot_060223 строка 29, 30
        if len(value) > 3:  # если длинна списка не соответствуе нужной - выводим ошибку класса строка 6, 14, 16
            raise ConvertionExecption(f'Некорректный запрос: слишком много аргументов!!!')
        elif len(value) < 3:
            raise ConvertionExecption(f'Некорректный запрос: недостаточно аргументов!!!')


class ErrorsOutput:  # класс ошибок контролирующий опечатки или ошибки при вводе
    @staticmethod  # декоратор позволяющий обращаться к методу класса напрямую файл TelegaBot_060223 строка 32
    def errors_output(quote, base, amount):  # передаем в функцию аргументы по отдельности файл TelegaBot стр. 31, 32
        if quote == base:   # если введены две одинаковые валюты, вызываем ошибку
            raise ConvertionExecption(f'Невозможно конвертировать одинаковые валюты: "{quote}" и "{base}"!')

        if quote not in key.keys():  # если введеная валюта отсутствует в списке доступных, выводим ошибку
            raise ConvertionExecption(f'Валюта "{quote}" отсутствует в списке доступных!!!\n'
                                      f'Список доступных валют --> /values')

        if base not in key.keys():  # если введеная валюта отсутствует в списке доступных выводим ошибку
            raise ConvertionExecption(f'Валюта "{base}" отсутствует в списке доступных!!!\n'
                                      f'Список доступных валют --> /values')
        try:  # если количество переводимой валюты не является числовым значением, выводим ошибку
            amount = float(amount)
        except ValueError:
            raise ConvertionExecption(f'Не удалось обработать количество "{amount}"')


class GetPrice:  # класс для получения доступа к валютным данным через API
    @staticmethod  # декоратор позволяющий обращаться к методу класса напрямую файл TelegaBot_060223 строка 33
    def get_price(quote, base, amount):  # передаем в функцию аргументы по отдельности файл TelegaBot стр. 31, 33
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={key[quote]}&tsyms={key[base]}').content
        converted = json.loads(r)  # декодируем полученные данные стр 41 в байтовом формате в json-формат
        text = f'Стоимость {amount} {key[quote]} равна {converted[key[base]] * float(amount)} {key[base]}'
        return text  # возвращаем сформированный текст стр 43 в метод get_price()
