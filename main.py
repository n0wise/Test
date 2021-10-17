# Тестовое задание Veeam Software - Junior Developer in QA, Задание 2 - синхронизация каталогов

import os
import logging
import time
from dirsync import sync

# Запрашиваем у пользователя путь для сохранения лога
logpath = str(input("Input log path like '/home/user/log_folder'\nLog file path: "))

# Настраиваем логирование
logging.basicConfig(
    level=logging.DEBUG,
    filename = r"" + logpath + "/" + "log",
    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    )
logging.info('Start logging')

# Функция запроса пути к каталогу-источнику, проверяем существует ли он
def s_path():
    s_path = str(input("Input source catalog path like '/home/user/source_folder'\nSource_path: "))
    while not os.path.exists(s_path):
        print('catalog not exists')
        s_path = str(input("Input source catalog path like '/home/user/source_folder'\nSource_path: "))
    return s_path

# Функция выполняет синхронизацию каталогов с заданным интервалом времени
def pereodic_sync(Tp):
    sync(source_path, target_path, 'sync', create=True, purge=True)
    time.sleep(Tp)

# Запрашиваем путь к катологу-источнику и передаем в функцию синхронизации
source_path = s_path()

# Запрашиваем у пользователя путь каталога-реплики
target_path = str(input("Inp target path like '/home/user/target_folder'\nTarget path: "))

# Запрашиваем у пользователя интервал синхронизации в секундах
Tp = int(input("Input sync interval in seconds like '1, 2, 3, 20, 100''\nSync interval, sec = "))

#Вызываем функциию переодической синхронизации
while True:
    pereodic_sync(Tp)