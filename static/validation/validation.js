import { submitBtn, usernameRegex, emailRegex } from "./const.js"

function bindAll(elements) {
    elements.forEach(e => {
        e[0].forEach(input => {
            submitBtn.addEventListener('click', (_) => e[1](input))
        })
    })
}

function validateUsername(event) {
    if (!usernameRegex.test(event.value)) {
        event.setCustomValidity('Username must start with one uppercase followed by any lowercase')
    } else if (event.value.length > 150) {
        event.setCustomValidity('Username length must be less than or equal to 150')
    } else {
        event.setCustomValidity('')
    }

    event.reportValidity()
}

function validateEmail(event) {
    if (!emailRegex.test(event.value)) {
        event.setCustomValidity('Wrong email input')
    } else if (event.value.length > 254) {
        event.setCustomValidity('Email length must be less than or equal to 254')
    } else {
        event.setCustomValidity('')
    }
}

function validateLogin(event) {
    if (event.value.length > 254) {
        event.setCustomValidity('Field length must be less than or equal to 254')
    } else {
        event.setCustomValidity('')
    }
}


const validatePairs = []

const usernameInputs = document.querySelectorAll('input.name')
const emailInputs = document.querySelectorAll('input.email')
const loginInputs = document.querySelectorAll('input.login')

validatePairs.push([usernameInputs, validateUsername])
validatePairs.push([emailInputs, validateEmail])
validatePairs.push([loginInputs, validateLogin])

bindAll(validatePairs)

