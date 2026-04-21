import { submitBtn, usernameRegex } from "./const.js"

function bindAll(elements) {
    elements.forEach(e => {
        submitBtn.addEventListener('click', (_) => validateUsername(e))
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

const usernameInputs = document.querySelectorAll('input.name')
bindAll(usernameInputs)

