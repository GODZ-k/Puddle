let flag = 1

// show and hide password
let password = document.getElementById('password')
let confirmpassword = document.getElementById('confirmpassword')
const showpassword = () => {
    if (password.type == 'text' &&
        confirmpassword.type == 'text') {
        password.type = 'password'
        confirmpassword.type = 'password'
    } else {
        password.type = 'text'
        confirmpassword.type = 'text'
    }
}

// show login page pasword
const showloginpassword = () => {
    if (password.type == 'text') {
        password.type = 'password'

    } else {
        password.type = 'text'
    }
}


// confirm password validation

function valid(elem) {
    if (elem.length > 0) {
        if (elem != password.value) {
            document.getElementById('valid').innerHTML = "Confirm password doesn't match"
            flag = 0
        } else {
            document.getElementById('valid').innerHTML = ""
            flag = 1
        }
    } else {
        document.getElementById('valid').innerHTML = "Pleaee enter confirm password"
        flag = 0
    }

}

// white space validation
let patten = /\s/g;

function mail(value) {
    const x = patten.test(value)
    if (x == true) {
        document.getElementById('whitespace').innerHTML = "Space isn't allowed"
        flag = 0
    } else {
        document.getElementById('whitespace').innerHTML = ""
        flag = 1
    }

}

function pass(value) {
    const x = patten.test(value)
    if (x == true) {
        document.getElementById("passwordspace").innerHTML = "Space isn't allowed"
        flag = 0
    } else {
        document.getElementById("passwordspace").innerHTML = ""
        flag = 1
    }
}


function validation() {
    if (flag == true) {

        return true
    } else {
        return false
    }
}