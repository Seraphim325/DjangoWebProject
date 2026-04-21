import { submitBtn, usernameRegex } from "./const.js"

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
    } else {
        event.setCustomValidity('')
    }

    event.reportValidity()
}


const validatePairs = []

const usernameInputs = document.querySelectorAll('input.name')
validatePairs.push([usernameInputs, validateUsername])

bindAll(validatePairs)

