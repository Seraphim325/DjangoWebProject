import { submitBtn } from "../const.js"

function validatePasswords() {
    const password1 = document.querySelector("#password1")
    const password2 = document.querySelector("#password2")

    if (password1.value !== password2.value) {
        password1.setCustomValidity('Passwords not equal')
        password2.setCustomValidity('Passwords not equal')
    } else {
        password1.setCustomValidity('')
        password2.setCustomValidity('')
    }

    password1.reportValidity()
    password2.reportValidity()
}

submitBtn.addEventListener('click', validatePasswords)