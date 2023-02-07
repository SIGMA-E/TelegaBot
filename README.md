# TelegaBot
This telegram bot for converting of currency EUR, USD, RUB.
Имя бота: SigmaBot

Найти его можно тут: t.me/Sigma_E_bot

Файл TelegaBot_060223.py основной для запуска телеграмм бота

Файл config.py содержит токен и список доступных валют в виде словаря

Файл extension.py содержит:

класс GetPrice для получения валютных данных через API и формирования результирующего текста сообщения

класс ErrorsInput и ErrorsOutput для поиска и вывода ошибок на вводе       

класс ConvertionExeption пустой для формирования типа ошибки в виде сообщения
