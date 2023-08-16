
<H1>🆃🅴🆇🆃-🅵🅾🆁🆄🅼.🅾🆁🅶 </H1>

<p align="center">
This repository contains files for the "text-forum.org" server. This project is open-source. 
The backend is built on the Fast API library using the Python 3.11.4 programming language. The frontend is written in HTML 5, CSS 3, and pure JavaScript. The database runs on the sqlite3 technology.
This forum has its own API for creating client applications targeted for various platforms.


List of URLs to access the API:

http://{server domain}/logins - returns a list of user logins

http://{server domain}/registrate/{login}/{password} - registers a new user

http://{server domain}/auth/{login}/{password} - authenticates the user and returns the session code

http://{server domain}/threads/1 - returns a list of threads created by users on the forum

http://{server domain}/mess/{thread id} - returns information about the messages in the thread with the provided id in the query string

http://{server domain}/session_check/{session code} - checks if the session code exists and returns the username associated with the session token




Данный репизиторий содержит в себе файлы для сервера "text-forum.org". Этот проект является open-source. 
Backend создан на основе библиотеки Fast Api на языке программирования Python 3.11.4 . Frontend написан на HTML 5, CSS 3  и чистом JavaScript. База данных работает на технологии sqlite3.
Данный форум имеет своё API для создания клиентских приложений, ориентированных для различных платформ. 


Список URL для обращения к API:

http://{домен сервера}/logins - возвращает список логинов пользователей

http://{домен сервера }/registrate/{логин}/{пароль} - регистрирует нового пользователя

http://{домен сервера}/auth/{логин}/{пароль} - аунтефицирует пользователя и возращает код его сессии

http://{домен сервера}/threads/1 - возвращает список тем, созданных пользователями на форуме

http://{домен сервера}/mess/{id темы} - возвращает информацию о сообщениях в теме с переданным в строке запроса id

http://{домен сервера}/session_check/{код сессии} - проверяет явлеятся код сессии существующим и возвращает имя пользователя привязанного к токену сессии


</p>