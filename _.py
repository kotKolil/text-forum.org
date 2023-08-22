import sqlite3 as sql
import sys
import random
import string
import pathlib
pathlib.Path(sys.argv[0]).parent  # абсолютный путь до каталога, где лежит скрипт

def info_users():
	# Подключение к базе данных
	conn = sql.connect('db.db')
	cursor = conn.cursor()

	# Выполнение SELECT запроса
	cursor.execute("SELECT * FROM users")
	data = cursor.fetchall()  # Получение всех строк результата запрос

	# Закрытие соединения с базой данных
	conn.close()

	return data

def gri():
	#unique indeficator of session
	uis = " "
	symbols = string.ascii_lowercase
	for i in range(random.randint(5,10)):
		uis += random.choice(symbols)
	return uis

print(info_users())


