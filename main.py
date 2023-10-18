#импортируем fastapi
from fastapi import *
from fastapi.responses import RedirectResponse as redirect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse as htm
from fastapi.responses import *
from typing import Optional
import sqlite3 as sql
import sys
import pathlib
import string 
import random
import time
import datetime
import requests as r
import aiosqlite
import asyncio
import json
from aiologger.loggers.json import JsonLogger

#создаём объект приложения
app = FastAPI()

#генератор индефикаторов сессии


logger = JsonLogger.with_default_handlers(
            level='DEBUG',
            serializer_kwargs={'ensure_ascii': False},
        )



#путь где лежит приложение
script_path = pathlib.Path(sys.argv[0]).parent


#добавляем статик файлы
app.mount("/static/", StaticFiles(directory="pages"))
app.mount("/js/", StaticFiles(directory="js"))
app.mount("/css/", StaticFiles(directory="css"))
app.mount("/smiles/", StaticFiles(directory="smiles"))




"""
#middleware for ip

@app.middleware("http")
def ip_check(request : Request , call_next):
	ip = request.client.host

	conn = sql.connect('db.db')
	cursor = conn.cursor()

	# Выполнение SELECT запроса
	cursor.execute("SELECT IP FROM banned_ips") 
	data = cursor.fetchall()  # Получение всех строк результата запрос

	# Закрытие соединения с базой данных
	conn.close()

	for i in data: 
		if i == ip:
			response = call_next(request)
			request  
	return call_next(request)

"""

	
async def  exccute(expression):
	async with aiosqlite.connect('db.db') as db:
		cursor = await db.execute(expression)
		data = await cursor.fetchall()
		await db.commit()
		await logger.info(f'был выполнен запрос {expression}')
	return data

def gcd():
    current_datetime = datetime.datetime.now()
    return current_datetime.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


#Generate random Id
def gri():
	#unique indeficator of session
	uis = " "
	symbols = "1234567890qwertyuiopasdfghjklzxcvbnm"
	for i in range(random.randint(5,10)):
		uis += random.choice(symbols)
	return uis




@app.get("/")
async def main(session: str = Cookie(None)):
	

	task = asyncio.create_task( exccute(f"SELECT * FROM users where IPS = ' {session}' "))
	data = await task
	if len(data) != 0: return FileResponse("pages/main.html")
	else: return FileResponse("pages/account.html")

@app.get("/logins")
async def logins():
	task = asyncio.create_task(exccute("SELECT USERNAME FROM users ORDER BY USERNAME"))
	raw = await task
	data = []
	for i in raw: data.append(i[0])
	return data
		

@app.get("/registrate/{login}/{password}")
async def reg(login, password):
	conn = sql.connect('db.db', timeout=7)
	cursor = conn.cursor()
	expression =  "SELECT USERNAME FROM users GROUP BY USERNAME "
	cursor.execute(expression)
	data = cursor.fetchall()
	conn.close()

	for i in data:
		if login == i[0]:
			return [403]

	else:


		ids = gri()
		task  = asyncio.create_task(  exccute("SELECT IPS FROM users ORDER BY USERNAME"))
		raw = await task
		data = []
		for i in raw: data.append(i[0])
		if ids in data: ids = gri()

		

		conn = sql.connect('db.db', timeout=7)
		cursor = conn.cursor()
		expression = """INSERT INTO users (USERNAME, PSWD, IPS) VALUES (?, ?, ?)"""
		params = (login, password, ids)
		cursor.execute(expression, params)
		conn.commit()
		conn.close()
		await logger.info(f'зарегистрирован {login} {password} {ids}')
		return [ids]

#аунтефикация
@app.get("/auth/{login}/{password}")
async def auth(password, login):


	task = asyncio.create_task(exccute(f"SELECT * FROM users where USERNAME =  '{login}' and PSWD = '{password}' "))
	data = await task
	if len(data) == 0: return ["403"]
	else: return ["200", data[0][1]]




@app.get("/threads")
async def threads():


	task = asyncio.create_task(exccute("SELECT * FROM  THD"))
	h = await task
	return h

@app.get("/thd/{d}")
def thd(d):
	return FileResponse("pages/thd.html")

@app.get("/mess/{ids}")
async def huy(ids):
	

	task= asyncio.create_task( exccute(f"SELECT * FROM  {ids}"))
	h = await task
	return h

@app.get("/session_check/{ids}")
async def ch_ses(ids):
	

	data = await  exccute(f"SELECT USERNAME , IPS FROM users where IPS = ' {ids}' ")
	if len(data) == 0: return ["404"]
	else: return [data[0][0] , ids]	


@app.get("/crt_thd/{session}/{theme}")
async def crt_thd(session, theme):
	

	task = asyncio.create_task( exccute(f"SELECT IPS FROM users where IPS = ' {session}'"))
	data = await task
	h = r.get(f"http://127.0.0.1:8000/session_check/{session}").json()[0]
	if len(data[0]) == 1: 
		ids = str(h)+theme+str(random.choice(range(1000,100000)))

		#вносим в таблицу информацию о создающемся треде
		conn = sql.connect('db.db', timeout=7)
		cursor = conn.cursor()
		expression = f"""INSERT INTO THD (CREATOR , THEM , TIME_CREATING , id) VALUES (?, ?, ?, ?)"""
		params = (h, theme, gcd() , ids)
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


		return [200]
	return [403]


@app.post("/send_message")
async def sm(request: Request):
	# json must looks as {user}/{message}/{thd}/{session}

	task  = asyncio.create_task( exccute("SELECT * FROM users"))
	data = await task
	js = await request.json()
	user = js[0]
	message = js[1]
	thd = js[2]
	session = js[3]
	for i in data:
		if i[0] == user and i[1][1:] == session:
			conn = sql.connect('db.db')
			expression = f"""INSERT INTO {thd} (sender, message, time) VALUES ('{user}' , '{message}', '{gcd}')"""
			conn.execute(expression)
			conn.commit()
			conn.close()
			return [200]
	return [403]


@app.get("/FAQ")
def FAQ(request : Request):
	

	ip = request.client.host
	if ip == "127.0.0.1":
		return HTMLResponse('Какой же ты не умный человек)))')
	else:
		try:
			g = r.get("http://ipwho.is/{ip}")
			if g.json()["country"] == "Russia":
				return FileResponse("pages/faqRU.html")
			else:
				return FileResponse("pages/faqEN.html")
		except:
			return FileResponse("pages/faqEN.html")

@app.get("/smile/{num}")
async def smiles(num:int):


	if num == 0:
		data = []
		task  = asyncio.create_task( exccute("SELECT * from smiles"))
		raw = await task
		for i in raw: data.append(i[0])
		return data
	elif num == 1:
		data = []
		task  = asyncio.create_task(exccute("SELECT * from smiles"))
		raw = await task
		for i in raw: data.append(i[0])

		html = """ """

		for i in data:
			html += f""" <img 
			onclick="insert_to_message('{i}');"

			src='http://127.0.0.1:8000/smiles/{i}.gif' />""" 

		return [html]

@app.get("/test")
def test():
	

	return htm("I am fine")

@app.get("/debug")
def debug(request : Request):
	return htm(f"{request.__dict__}")
