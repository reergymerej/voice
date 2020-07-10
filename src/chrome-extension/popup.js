'use strict'

const textarea = document.getElementById('textarea')
const cancel = document.getElementById('cancel')
const submit = document.getElementById('submit')
const error = document.getElementById('error')

cancel.addEventListener('click', () => {
  window.close()
})

const setText = (el, text) => el.innerText = text

const beforeSave = () => {
  setText(submit, 'saving...')
  submit.disabled = true
}

const afterSave = (_response) => new Promise((resolve) => {
    setText(submit, 'saved')
    setTimeout(() => {
      submit.disabled = false
      textarea.value = ''
      window.close()
      resolve()
    }, 2000)
})

const onSaveError = (_err) => {
  setText(submit, 'It didn\'t work.')
}

const getText = () => (textarea.value || '').trim()

const onSave = () => {
  const text = getText()
  beforeSave()
  const url = 'https://lmeimzkewb.execute-api.us-east-1.amazonaws.com/prod'
  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      text
    }),
  }).then(x => x.json())
    .then(afterSave)
    .catch(onSaveError)
}

const onKeyUp = () => submit.disabled = getText().length === 0

submit.addEventListener('click', onSave)
textarea.addEventListener('keyup', onKeyUp)
textarea.addEventListener('change', onKeyUp)
textarea.addEventListener('blur', onKeyUp)
