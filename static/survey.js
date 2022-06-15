function getCookie(name) {
   let cookieValue = null;
   if (document.cookie && document.cookie !== '') {
       const cookies = document.cookie.split(';');
       for (let i = 0; i < cookies.length; i++) {
           const cookie = cookies[i].trim();
           // Does this cookie string begin with the name we want?
           if (cookie.substring(0, name.length + 1) === (name + '=')) {
               cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
               break;
           }
       }
   }
   return cookieValue;
}

async function buttonClickHandler() {
   const postForm = document.querySelector("#addQuestionForm");
   formData = new FormData(postForm);
   // API CALL
   const response = await fetch('', {
      method: "POST",
      credentials: "same-origin",
      headers: {
         "X-Requested-With": "XMLHttpRequest",
      },
      body: formData,
   });
   const json = await response.json();
   if (json.Success == true) {
      postForm.reset();
      const options = document.getElementById('options');
      options.innerHTML = ""
      number_of_question += 1
      questionElement = document.getElementById('question_count')
      questionElement.innerText = `Questions: ${number_of_question}`
   }
}

async function verifyEmail(pk) {
   let email = document.getElementById('email').value;
   const csrftoken = getCookie('csrftoken');
   // API CALL
   const response = await fetch(`/email-verify/${ pk }/`, {
      method: "POST",
      credentials: "same-origin",
      headers: {
         "X-Requested-With": "XMLHttpRequest",
         'X-CSRFToken': csrftoken
      },
      body: JSON.stringify(email),
   });
   const json = await response.json();
   let emailHelp = document.getElementById('emailHelp')
   let submitBtn = document.getElementById('submitBtn')
   if (json.Success == true) {
      emailHelp.innerText = "Email Address Already Exists";
      submitBtn.disabled = true
   }
   else{
      emailHelp.innerText = "Email Address Available";
      submitBtn.disabled = false
   }
}

let alert = document.getElementById('alert')
if (alert != null) {
   setTimeout(() => {
      alert.classList.add('d-none')
   }, 2000);
}