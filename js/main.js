//функция для регистрации/входа
// Функция для установки куки


function sleep(seconds) {
  const ms = seconds * 1000;
  const start = new Date().getTime();
  let currentTime = null;
  do {
    currentTime = new Date().getTime();
  } while (currentTime - start < ms);
}

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
  setCookie("cook", "1", 666);
}

async function get_threads () {
  const div = document.getElementById("thd");
  const rezultat = await fetch("/threads");
  let list = await rezultat.json();
  var news = "";
  for (let i = 0 ; i < list.length; i++ ) {
    var arr = list[i];
    news = news + 
      `<div><strong>тема : ${arr[1]}</strong> <p> за авторством ${arr[0]}</p>
      <button onclick="window.location.replace('thd/${arr[3]}');">тык для перехода</button></div>`;
  }
  if (news !== div.innerHTML) {
    div.innerHTML = news;
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

function cc() {
  try {
    var f = getCookieValue("cook");
    if (f == "1"){
      console.log("братиша я тебе покушать принёс...");
      hide();
    }
  }
  catch (err) {
    console.log(err);
  }
}


async function get() {
  // получаем данные с сервера

  //получение элементов формы
  const login = document.getElementById('login');
  const password = document.getElementById('password');
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
        const authResponse = await fetch(`/registrate/${login.value}/${password.value}`);
        const authResult = await authResponse.json();


        console.log(authResult);
        
        if (authResult[0] == "403") {
          status.style.color = "red";
          status.innerHTML = "Этот ник занят";
        }
        else {
          setCookie("session", authResult[0], 666);
          //window.location.replace("/");
        }

      }
    } else {
      //вход в систему

      //отправка данных на сервер для проверки
      const authResponse = await fetch(`/auth/${login.value}/${password.value}`);
      const authResult = await authResponse.json();
      console.log(authResult);
      if (authResult[0] != "403") {
        setCookie("session", authResult[1] ,666);
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





 async function get_msg() {
  const url = window.location.href;


  const block = document.getElementById("mess")

  var ids = url.split("/")

  var response = await fetch(`/mess/${ids[ids.length-1]}`);
  var data = await response.json();

  


  var old = "";
  for (var i = 0; i < data.length; i++) {

//for deleting - 1 argument user, 2 argument - sender
    old += `



<table>
  <tr>
    <th style="background-color: #ccc; width:  40px;">


<div id="mess_block">
  <div>
    <p>${data[i][0]}</p>
    <p>${data[i][2]}</p>
  </div>


    </th>
    <th style="vertical-align:top; padding-top:5px;>   <span id="message">
    ${data[i][1]}
    </span>
    </th>
  </tr>
  <tr>
  <th>
  <button onclick="answer('${data[i][0]}');" ,  style="width:100%; height:100%;" >Ответить</button>
  </th>
  </tr>
</table>



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
  var url = window.location.href;

  url = url.split("/");
  url = url[url.length-1]

  var textarea = document.getElementById("input")
  var input = document.getElementById("input").value;
  var ine = document.getElementById("in")
  console.log(input);

  var ids = getCookieValue("session");
  console.log(ids);
  
  var response = await fetch(`/session_check/${ids}`);
  response = await response.json();
  console.log(response);

  data = [response[0] , `${input}` , url ,getCookieValue("session")]



  if (textarea.value == "") {
    ine.innerHTML = "ваше сообщение не должно быть пустым";

  } 

  if (response[0] === 404) {
    window.location.replace("/");
  } else {

  console.log(data);

  var response = await fetch("/send_message", {
    method: 'POST', // или 'PUT'
    body: JSON.stringify(data), 
  });

    //await fetch(`/send_message/${response[0]}/${input}/${url}/${getCookieValue("session")}`);
    textarea.value = "";
    
  }
    response = await response.json();

    console.log(response);

}


async function crt_thd() {
  var theme = document.getElementById("theme").value;
  var text = document.getElementById("text");
  var session = getCookieValue("session");

  //отправка на сервер
  var response  = await fetch(`/crt_thd/${session}/${theme}`);
  window.location.replace("/")

}


async function get_smiles() {

  const response = await fetch("/smile/1");
  var data = await response.json();
  var html = data[0]
  console.log(data);

  var smileBlock = document.getElementById("smile");
  smileBlock.innerHTML = html;
}

function copyToClipboard(text) {
  const textarea = document.createElement('textarea');
  
  textarea.value = text;
  document.body.appendChild(textarea);
  textarea.focus();
  textarea.select();
  
  document.execCommand('copy');
  document.body.removeChild(textarea);

}

function insert_to_message (ids) {
  message_field = document.getElementById("input");
  message_field.value = `<img src="http://127.0.0.1:8000/smiles/${ids}.gif" />` + message_field.value;



 }



function answer(ids) {
  message_field = document.getElementById("input");
  message_field.value = `<p id="answr">Answer to ${ids} </p>` + message_field.value;



 }

