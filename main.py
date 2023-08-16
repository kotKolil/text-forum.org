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

#создаём объект приложения
app = FastAPI()

#генератор индефикаторов сессии
def gri():
	#unique indeficator of session
	uis = " "
	symbols = string.ascii_uppercase
	for i in range(random.randint(5,10)):
		uis += random.choice(symbols)
	return uis



#добавляем статик файлы
app.mount("/static/", StaticFiles(directory="pages"))
app.mount("/js/", StaticFiles(directory="js"))
app.mount("/css/", StaticFiles(directory="css"))



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
	logins = {"petya123"}
	return logins
		
#регистрация
@app.get("/registrate/{login}/{password}")
def reg(login, password):
  conn = sql.connect('db.db', timeout=7)
  cursor = conn.cursor()

  expression = (f"""INSERT INTO users (USERNAME , PSWD) VALUES ('{login}', '{password}')""") 

  # Выполнение INSERT запроса
  cursor.execute(expression)
  conn.commit()

  # Закрытие соединения с базой данных
  conn.close()

#аунтефикация
@app.get("/auth/{login}/{password}")
def auth(password, login):
	data = info_users()
	try:
		for i in data:
			if i[0] == login and i[len(i)-1] == password:
				#возращаем код сессии юзера
				return {"code":"em3mie"}
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
			return {data[i][0]:data[i][3].split(",")[0]}
	return ["404"]
@app.get("/send_message/{user}/{message}")
def send(user, message):
	pass   