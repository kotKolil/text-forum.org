//функция для регистрации/входа
// Функция для установки куки
function setCookie(name, value, days) {
  const date = new Date();
  date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
  const expires = "expires=" + date.toUTCString();
  document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

//funktion about coockie-file
function hide() {

  dib = document.getElementById('report');
  dib.id = "hide";
  document.cookie = "cook" + "=" + "1"+ ";";
  document.cookie = "cook" + "=" + "1"+ ";";
}

async function get_threads () {
  const div = document.getElementById("thd");
  const rezultat = await fetch("/threads/1");
  let list = await rezultat.json();
  for (let i = 0 ; i < list.length; i++ ) {
    var arr = list[i];
    div.innerHTML = div.innerHTML + 
      `<div><strong>тема : ${arr[1]}</strong> <p> за авторством ${arr[0]}</p>
      <button onclick="window.location.replace('thd/${arr[3]}');">тык для перехода</button></div>`;
  }
}

//функция для регистрации/входа
// Функция для установки куки
function setCookie(name, value, days) {
  const date = new Date();
  date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
  const expires = "expires=" + date.toUTCString();
  document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

function getCookieValue(cookieName) {
    var cookieValue = "";
    var cookies = document.cookie.split(";");

    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, cookieName.length + 1) === (cookieName + "=")) {
            cookieValue = decodeURIComponent(cookie.substring(cookieName.length + 1));
            break;
        }
    }

    return cookieValue;
}


async function get() {
  // получаем данные с сервера

  //получение элементов формы
  const login = document.getElementById('login');
  const password = document.getElementById('password');
  const email = document.getElementById("email");
  const status = document.getElementById("error");
  const method = document.getElementById("action");

  //валидация данных

  if (login.value.length === 0 || password.value.length === 0) {  
    status.style.color = "red";
    status.innerHTML = "Логин и пароль обязательны для заполнения";
  } else {
    if (method.value === "a") {
      //регистрация
      if (password.value.length < 11) {
        status.style.color = "red";
        status.innerHTML = "минимальная длина пароля 11 символов";
      } else {
        //регистрация аккаунта
        console.log("регистрация");

        //отправка данных на проверку 
        const authResponse = await fetch(`/auth/${login.value}/${password.value}`);
        const authResult = await authResponse.json();


        console.log(authResult);
        
        if (authResult[0] == "403") {
          status.style.color = "red";
          status.innerHTML = "Этот ник занят";
        }
        else {
          setCookie("session", authResult[1], 666);
          //window.location.replace("/");
        }

      }
    } else {
      //вход в систему

      //отправка данных на сервер для проверки
      const authResponse = await fetch(`/auth/${login.value}/${password.value}`);
      const authResult = await authResponse.json();
      console.log(authResult);
      if (authResult["code"] != "403") {
        setCookie("session", "em3mie",100);
        window.location.replace('/');
      } else {
        console.error('Ошибка:', authResult);
        status.style.color = "red";
        status.innerHTML = "Неправильный пароль или логин";
        console.log("неправильный пароль или логин");
      }
    }
  }
}



//this funktion change main page to thread! It is awesome!
async function ctt (ids) {


  const response = await fetch(`/mbi/${ids}`)
  const data = await response.json();

    for (let i = 0 ; i < data.length-1; i++ ) {
    var arr = list[i]
    console.log(arr[0]);
    console.log(arr[1]);
    div.innerHTML = div.innerHTML + `
    <div>
    <span>

    <strong>

    

    </strong>

    </span>


    </div>

    `
  }
}



 async function get_msg() {
  const url = window.location.href;
  console.log(url);

  const block = document.getElementById("mess")

  var ids = url.split("/")
  console.log(ids[ids.length-1])

  var response = await fetch(`/mess/${ids[ids.length-1]}`);
  var data = await response.json();
  console.log(data);


  var old = "";
  for (var i = 0; i < data.length; i++) {

    old += `
      <div id="mess_block">
        <strong>${data[i][0]} в ${data[i][2]}</strong>
        <div id="message"> 
          ${data[i][1]}
        </div>
      </div>
    `;
  }
  if (old !== block.innerHTML) {
    block.innerHTML = old;
  }
}








function home() {

window.location.replace("/");
};

async function send_message() {
  var input = document.getElementById("input").value;
  console.log(input);

  var ids = getCookieValue("session");
  console.log(ids);
  
  var response = await fetch(`/session_check/${ids}`);
  response = await response.json();
  console.log(response);
  
  if (response[0] === 404) {
    window.location.replace("/");
  } else {
    await fetch(`/send_message/${response[0]}/${response[1]}`);
    console.log("отправка");
  }
}





























