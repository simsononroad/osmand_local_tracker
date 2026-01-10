const login_form = document.getElementById("login")
const register_form = document.getElementById("register")

register_form.style = "display: None;"

function NoUser(){
    const login_form = document.getElementById("login")
    const register_form = document.getElementById("register")

    login_form.style = "display: None;"
    register_form.style = "display: block;"
}

function HaveUser(){
    const login_form = document.getElementById("login")
    const register_form = document.getElementById("register")

    login_form.style = "display: block;"
    register_form.style = "display: none;"
}