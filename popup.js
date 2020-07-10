'use strict'

const textarea = document.getElementById('textarea')
const cancel = document.getElementById('cancel')
const submit = document.getElementById('submit')

cancel.addEventListener('click', () => {
  window.close()
})

submit.addEventListener('click', () => {
  const text = (textarea.value || '').trim()
  fetch('boop.beep.cork', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      text
    }),
  }).then(x => x.json())
    .then(x => console.log(x))
    .catch(error => console.log(error))
    // .finally(() => window.close())
})
