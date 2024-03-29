<h2><span id="litera">T</span>ext-forum.org</h2>
<p id="red">Минималистичный анонимный форум на любые темы</p>
<hr>

<p align="center">




This repository contains files for the <strong>Text Forum</strong> server. This project is open-source. 
The backend is built on the <strong>Fast API</strong> library using the <strong>Python 3.11.4</strong> programming language. The frontend is written in <strong>HTML 5</strong>, <strong>CSS 3</strong>, and pure <strong>JavaScript</strong>. The database runs on the <strong>sqlite3</strong> technology.
This forum has its own API for creating client applications targeted for various platforms.


Instructions for starting the server:
<ol>
  <li>System requirements required: Windows</li>
  <li>Open the command prompt</li>
  <li>Go to the <code>venv/Scripts</code> folder</li>
  <li>Run <code>activate.bat</code></li>
  <li>Go back to the Forum folder</li>
  <li>Write the following command: <code>uvicorn main:app --reload</code></li>
</ol>

Installing libraries for server operation:
<ol>
  <li>Open the Command Prompt</li>
  <li>Go to the Forum folder</li>
  <li>Make sure that there is an Internet connection</li>
  <li>Run: <code>pip install -r requirements.txt</code></li>
</ol>


List of URLs to access the API:
<ul>
  <li><code>http://{server_domain}/logins</code> - returns a list of user logins</li>
  <li><code>http://{server_domain}/registrate/{login}/{password}</code> - registers a new user</li>
  <li><code>http://{server_domain}/auth/{login}/{password}</code> - authenticates the user and returns the session code</li>
  <li><code>http://{server_domain}/threads/1</code> - returns a list of threads created by users on the forum</li>
  <li><code>http://{server_domain}/mess/{thread_id}</code> - returns information about the messages in the thread with the provided ID in the query string</li>
  <li><code>http://{server_domain}/session_check/{session_code}</code> - checks if the session code exists and returns the username associated with the session token</li>
</ul> 
<li>http://{server domain}/threads/1 - returns a list of topics created by users on the forum</li>
<li>http://{server domain}/mess/{topic id} - returns information about messages in the topic with the topic id passed in the query string </li>
<li>http://{server domain}/session_check/{session code} - checks if the session code exists and returns the username associated with the session token</li>
<li> <code> http://crt_thd /{session}/{theme}</code> - creating a thread. Session - user 's session code , theme - thread theme without !"№;%:?*(()~~` " </li>
<li> <code> http://{domain}/send_message </code> - POST method for sending messages in thread; accepts json of the following type: <p> <code> {user}/{message}/{thread id}/{session of user} </code> </li>


<H3>Docker</H3>
<p>For those who use Docker technologies, I have prepared a Dockerfile. To create a dockerfile, write this:</p>
<code>sudo docker build -t Forum </code>
<p>To run this container:</p>
<code>sudo docker run -p 8080:8000 forum</code>


<H3>Application Testing</H3>

To run the application test, write the following command:

<code>sudo pytest -v test_app.py</code>

<hr>

Инструкция к запуску сервера:
<ol>
  <li>Необходимы требования к системе: Windows</li>
  <li>Откройте командную строку</li>
  <li>Перейдите в папку <code>venv/Scripts</code></li>
  <li>Запустите <code>activate.bat</code></li>
  <li>Вернитесь в папку Forum</li>
  <li>Пропишите следующую команду: <code>uvicorn main:app --reload</code></li>
</ol>

Установка библиотек для работы сервера:
<ol>
  <li>Откройте Командную строку</li>
  <li>Перейдите в папку Forum</li>
  <li>Убедитесь в присутствии подключения к Интернет</li>
  <li>Пропишите: <code>pip install -r requirements.txt</code></li>
</ol>

Данный репозиторий содержит в себе файлы для сервера <strong>Text Forum</strong>. Этот проект является <strong>open-source</strong>. 
Backend создан на основе библиотеки <strong>Fast API</strong> на языке программирования <strong>Python 3.11.4</strong>. Frontend написан на HTML 5, CSS 3 и чистом JavaScript. База данных работает на технологии <strong>sqlite3</strong>.
Данный форум имеет своё API для создания клиентских приложений, ориентированных для различных платформ. 


Список URL для обращения к API:
<ul>
  <li><code>http://{домен_сервера}/logins</code> - возвращает список логинов пользователей</li>
  <li><code>http://{домен_сервера}/registrate/{логин}/{пароль}</code> - регистрирует нового пользователя</li>
<li>http://{домен сервера}/auth/{логин}/{пароль} - аунтефицирует пользователя и возращает код его сессии </li>

<li>http://{домен сервера}/threads/1 - возвращает список тем, созданных пользователями на форуме</li>
<li>http://{домен сервера}/mess/{id темы} - возвращает информацию о сообщениях в теме с переданным в строке запроса id темы  </li>
<li>http://{домен сервера}/session_check/{код сессии} - проверяет явлеятся код сессии существующим и возвращает имя пользователя привязанного к токену сессии</li>
<li> <code> http://crt_thd/{session}/{theme}</code> - создание треда. Session - код сесси пользователя , theme - тема треда без !"№;%:?*(()~~` " </li>
<li> <code> http://{домен}/send_message </code> - POST метод; принимает json такоого вида: <p> <code> {user}/{message}/{thd id}/{session of thread} </code> </li>

</ul>

<H3>Docker</H3>
<p> Для тех, кто использует технологии Docker, я подготовил Dockerfile. Для создания dockerfile пропишите это:
</p>
<code>sudo docker build -t Forum </code>
<p>Для запуска контейнера</p>
<code>sudo docker run -p 8080:8000 forum</code>


<H3>Тестинг приложения</H3>

Чтобы запустить тест приложения пропишите следующую команду:

<code>sudo pytest -v test_app.py</code>





