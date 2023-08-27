import json
import sqlite3 as sql
import os
import requests as r
import logging
import time 
import json

session = ""
password = "qwerty"
login = "petya12345"
thread_id = ""

def test_start():
	f = time.time()
	h = r.get("http://127.0.0.1:8000/test")
	t = time.time()
	assert h.text == "I am fine" 
	logger = logging.getLogger()
	logger.info(f"App susseful working. It war responsed in {t-f} seconds")

def test_reg():
	global session
	logger = logging.getLogger()

	f = time.time()
	h = r.get(f"http://127.0.0.1:8000/registrate/{login}/{password}")
	t = time.time()

	assert h.json() != [403]
	session = h.json()[0]

	logger.info(f"""The registration test has been passed. The registration request was completed in {t-f} seconds.
	 Session code: {session}""")

def test_double_reg():
	logger = logging.getLogger()

	f = time.time()
	h = r.get(f"http://127.0.0.1:8000/registrate/{login}/{password}")
	t = time.time()

	assert h.json() == [403]

	logger.info(f"""The registration test with the same data has been passed. The registration request was completed in {t-f} seconds.""")

def test_get_logins():
	logger = logging.getLogger()


	f = time.time()
	h = r.get("http://127.0.0.1:8000/logins")
	t = time.time()

	assert h.status_code == 200

	logger.info(f"The API for getting user logins is working fine. The request was executed in {t-f} seconds")

def test_get_list_of_thd():
	logger = logging.getLogger()


	f = time.time()
	h = r.get("http://127.0.0.1:8000/logins")
	t = time.time()

	assert h.status_code == 200

	logger.info(f"The API for getting list of user`s threads is working fine. The request was executed in {t-f} seconds")

def test_get_list_of_thd():
	logger = logging.getLogger()


	f = time.time()
	h = r.get("http://127.0.0.1:8000/FAQ")
	t = time.time()

	assert h.status_code == 200

	logger.info(f"The API for getting list of user`s threads is working fine. The request was executed in {t-f} seconds")



def test_auth():
	logger = logging.getLogger()

	f = time.time()
	h = r.get(f"http://127.0.0.1:8000/auth/{login}/{password}")
	t = time.time()

	assert h.json()[0] == "200" and h.json()[1] == session


	logger.info(f"""The API for authentication works fine. The authentication request was completed in {t-f} seconds.
	 Session code: {session}""")



def test_create_thd_api():
	session = "qwerty"
	logger = logging.getLogger()

	f = time.time()
	h = r.get(f"http://127.0.0.1:8000/crt_thd/{session}/other")
	h2 = r.get(f"http://127.0.0.1:8000/crt_thd/qwert/other")
	t = time.time()

	assert h.json().json()[0] == 200 and h2.json()[0] == 403

	loger.info(f"The thread creation API is working fine. Request was completed in {t-f} seconds. Session code: {session}")


def test_send_message_to_thread_and_database_as_file():
	logger = logging.getLogger()

	#creating table for thread
	conn = sql.connect('db.db', timeout=7)
	cursor = conn.cursor()
	expression = """INSERT INTO THD (CREATOR , THEM , TIME_CREATING , id) VALUES (?, ?, ?, ?)"""
	params = (login, "other", "01.01.00.12.00.00" , "qwerty")
	cursor.execute(expression, params)
	conn.commit()
	conn.close()



	
	conn = sql.connect('db.db', timeout=7)
	cursor = conn.cursor()
	expression = """
CREATE TABLE "qwerty" (
	"sender"	TEXT,
	"message"	TEXT,
	"time"	TEXT
);
			"""
	cursor.execute(expression)
	conn.commit()
	conn.close()


	data = [
    login,
    'HI',
    "qwerty",
    session

    
]


	f = time.time()

	data = json.dumps(data)

	h = r.post('http://127.0.0.1:8000/send_message', data=data)


def test_delete_testing_data_from_data_base():
    log = logging.getLogger()
    conn = sql.connect('db.db')

    # Создаем курсор, чтобы выполнить SQL-запросы
    cursor = conn.cursor()

    # Название таблицы, в которой нужно удалить данные
    table_name = 'table_name'

    # SQL-запрос на удаление всех данных в таблице
    expression_list = ["""DELETE FROM users where USERNAME = 'petya12345'""",
                       f"""DELETE FROM THD WHERE id = 'qwerty'""",
                       f"""DROP TABLE qwerty"""]

    # Выполняем SQL-запрос
    for expression in expression_list:
        cursor.execute(expression)

    # Применяем изменения в базе данных
    conn.commit()

    # Закрываем соединение с базой данных
    conn.close()

    log.info("The data created during testing was deleted successfully from the database")

    assert 1 == 1