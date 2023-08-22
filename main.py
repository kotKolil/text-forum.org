#импортируем fastapi
from fastapi import *
from fastapi.responses import RedirectResponse as redirect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse as htm
from fastapi.responses import *
from typing import Optional
from fastapi import FastAPI, HTTPException
import sqlite3 as sql
import sys
import pathlib
script_path = pathlib.Path(sys.argv[0]).parent  # абсолютный путь до каталога, где лежит скрипт
import string 
import random
import time
import datetime


#создаём объект приложения
app = FastAPI()

#генератор индефикаторов сессии




#добавляем статик файлы
app.mount("/static/", StaticFiles(directory="pages"))
app.mount("/js/", StaticFiles(directory="js"))
app.mount("/css/", StaticFiles(directory="css"))
app.mount("/icons", StaticFiles(directory="icons"))

def gcd():
    current_datetime = datetime.datetime.now()
    return current_datetime.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

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
	symbols = string.ascii_lowercase + "1234567890~!@#$%^&*())_{}:<>??"
	for i in range(random.randint(5,10)):
		uis += random.choice(symbols)
	return uis


def list_thd():
	# Подключение к базе данных
	conn = sql.connect('db.db')
	cursor = conn.cursor()

	# Выполнение SELECT запроса
	cursor.execute("SELECT * FROM  THD")
	data = cursor.fetchall()  # Получение всех строк результата запрос

	# Закрытие соединения с базой данных
	conn.close()

	return data


@app.get("/")
def main(session : str | None = Cookie(default=None)):

	
    data = info_users()

    for i in data:
    	ses = i[3]
    	ses = ses.split(",")
    	for h in ses:
    		if h == session:
	            response = FileResponse("pages/main.html")
	            return response
    response = FileResponse("pages/account.html")
    return response
    





@app.get("/logins")
def logins():
	data = info_users()
	logins = []
	for i in data:
		logins.append(i[0])
	return logins
		

@app.get("/registrate/{login}/{password}")
def reg(login, password):
	data = info_users()
	for i in data:
		if i[0] == login:
			return {"403":"уже есть"}
	ids = gri()
	for i in data:
		if i[3] == ids:
			ids = gri()

	conn = sql.connect('db.db', timeout=7)
	cursor = conn.cursor()
	expression = """INSERT INTO users (USERNAME, PSWD, IPS) VALUES (?, ?, ?)"""
	params = (login, password, ids)
	cursor.execute(expression, params)
	conn.commit()
	conn.close()
	return ["200",ids]

#аунтефикация
@app.get("/auth/{login}/{password}")
def auth(password, login):
	data = info_users()
	try:
		for i in data:
			if i[0] == login and i[len(i)-1] == password:
				#возращаем код сессии юзера
				return {"code":i[3].split(",")[0]}
			else:
				return {"code":"403"}
	except Exception as e:
		return {"4f":e}

@app.get("/threads/{a}")
def threads(a: str):  # добавляем аннотацию типа данных
    if a == "1":
    	return list_thd()
    else:
        raise HTTPException(
            status_code=400,
            detail="number not defined",
            headers={"header": "400"},
        )
@app.get("/thd/{d}")
def thd(d):
	return FileResponse("pages/thd.html")

@app.get("/mess/{ids}")
def huy(ids):

	conn = sql.connect('db.db')
	cursor = conn.cursor()

	# Выполнение SELECT запроса
	cursor.execute(f"SELECT * FROM  {ids}")
	data = cursor.fetchall()  # Получение всех строк результата запрос

	# Закрытие соединения с базой данных
	conn.close()

	return data

@app.get("/session_check/{ids}")
def ch_ses(ids):
	data = info_users()
	for i in range(len(data)):
		if data[i][3].split(",")[0] == ids:
			return [data[i][0],data[i][3].split(",")[0]]
	return ["404"]
@app.get("/send_message/{user}/{message}/{thd}/{session}")
def send(user, message, thd, session):
	data = info_users()
	for i in data:
		if i[0] == user and i[3].split(",")[0] == session:
			conn = sql.connect('db.db', timeout=7)
			cursor = conn.cursor()
			expression = f"""INSERT INTO {thd} (sender, message, time) VALUES (?, ?, ?)"""
			params = (user, message, gcd())
			cursor.execute(expression, params)
			conn.commit()
			conn.close()
			return [200]
	return [403] 


@app.get("/crt_thd/{session}/{theme}")
def crt_thd(session, theme):
	data = info_users()
	for i in data:
		if i[3].split(",")[0] == session:
			ids = i[0]+theme+str(random.choice(range(1000,100000)))

			#вносим в таблицу информацию о создающемся треде
			conn = sql.connect('db.db', timeout=7)
			cursor = conn.cursor()
			expression = f"""INSERT INTO THD (CREATOR , THEM , TIME_CREATING , id) VALUES (?, ?, ?, ?)"""
			params = (i[0], theme, gcd() , ids)
			cursor.execute(expression, params)
			conn.commit()
			conn.close()


			#создаём таблицу для треда
			conn = sql.connect('db.db', timeout=7)
			cursor = conn.cursor()
			expression = f"""
CREATE TABLE {ids} (
	"sender"	TEXT,
	"message"	TEXT,
	"time"	TEXT
);
			"""
			cursor.execute(expression)
			conn.commit()
			conn.close()

			return ["200"]
	return ["403"]


