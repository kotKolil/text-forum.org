import sqlite3
import sqlite3 as sql
import sys
import random
import string
import os
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


def insert_filenames_to_db(path):
    # Устанавливаем соединение с базой данных
    conn = sqlite3.connect("db.db")
    cursor = conn.cursor()

    # Получаем список файлов без расширений из указанной папки
    filenames = [os.path.splitext(file)[0] for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    print(filenames)

    # Вставляем имена файлов в колонку 'id' таблицы в базе данных
    for filename in filenames:
        cursor.execute(f"""INSERT INTO smiles (ids) VALUES ('{filename}')""")

    # Сохраняем изменения
    conn.commit()

    # Закрываем соединение
    conn.close()

insert_filenames_to_db("C:/Forum/smiles", )




