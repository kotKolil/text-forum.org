import sqlite3 as sql
import sys
import pathlib
pathlib.Path(sys.argv[0]).parent  # абсолютный путь до каталога, где лежит скрипт

def info_users(ip: int = "0.0.0.0"):
	# Подключение к базе данных
	conn = sql.connect('db.db')
	cursor = conn.cursor()

	# Выполнение SELECT запроса
	cursor.execute(''' INSERT INTO users (USERNAME, PSWD) VALUES (`masha123`, `2G4__b__3qj`) ''')
	data = cursor.fetchall()  # Получение всех строк результата запроса
	#print(data)

	# Закрытие соединения с базой данных
	conn.close()


print(info_users())