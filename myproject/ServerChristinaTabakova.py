# -*- coding: utf-8 -*-

import socket # Для работы с сокетами используем модуль socket.

socket = socket.socket() # Создаем сокет.

socket.bind(("localhost", 8000)) # Привязываем сокет к адресу моего компьютера и к порту.

# С помощью метода listen мы запустим для данного сокета режим прослушивания.
# Метод принимает один аргумент — максимальное количество подключений в очереди.
socket.listen(1)

while True:

    # Принимаем подключение с помощью метода accept, который возвращает кортеж с двумя элементами: новый сокет и адрес клиента.
    # Именно этот сокет и будет использоваться для приема и посылке клиенту данных.
    newsocket, address = socket.accept()

    # Мы в бесконечном цикле принимаем 1024 байт данных с помощью метода recv.
    # Если данных больше нет, то этот метод ничего не возвращает.
    # Таким образом мы можем получать от клиента любое количество данных.

    # Используем для получения данных метод recv, который в качестве аргумента принимает количество байт для чтения.
    data = newsocket.recv(1024)  # Читаем порциями по 1024 байт (или 1 кб).

    # В data содержится сообщение с помощью метода split(), разделяем сообщение на пробелы
    # и записываем преобразованное сообщение в переменную.
    pathToTheFile = data.split('\n')[0].split(' ')[1]

    # В переменную записываем первый элемент списка.
    pathToTheFile = pathToTheFile[1:]

    # Если переменная пустая, то переменной присваиваем новое название.
    if(pathToTheFile == ""):
        pathToTheFile ="index.html"

    # Открываем файл по новому пути.
    file = open(pathToTheFile)

    # Посылаем клиенту (" Протокол(HTTP)/Версия(1.1), Код Состояния(200) Пояснение(ОК)
    # - Стандартный ответ, подтверждающий согласие на действие по запросу,
    # передаем текстовый документ в размере html + передаем файл)
    newsocket.send(b'HTTP/1.1 200 OK\nContent-Type: text/html\n\n\n' + file.read())

    # Закрываем файл.
    file.close()

    # Закрываем соединение.
    newsocket.close()

# Закрываем сокет.
socket.close()




