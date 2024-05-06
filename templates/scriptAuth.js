function Login() {
    loginEl = document.getElementById("usernameInput");
    login = loginEl.value;
    passwordEl = document.getElementById("passwordInput");
    password = passwordEl.value;
    if (login == "admin" && password == "12345") {
        window.open("admin.html", "_self");
    } else if(login == "user" && password == "00000"){
        window.open("user.html", "_self");
    } else {
        loginEl.style.background = "red";
        passwordEl.style.background = "red";
        alert("Неверный логин или пароль!")
    }
}

function Reset() {
    loginEl = document.getElementById("usernameInput");
    loginEl.value = "";
    passwordEl = document.getElementById("passwordInput");
    passwordEl.value = "";
    loginEl.style.background = "white";
    passwordEl.style.background = "white";
}

function changeBg(id, color) {
    enterEl = document.getElementById(id);
    enterEl.style.background = color;
    enterEl.style.borderRadius = "5px"
}