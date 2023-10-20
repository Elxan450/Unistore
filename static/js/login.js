let loginForm = document.getElementById('login-form')
loginForm.addEventListener('submit', async function(event){
    let postData = {
        'username': loginForm.username.value,
        'password': loginForm.password.value,
    } 

    let response = await fetch('http://localhost:8000/auth/token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken" : loginForm.csrfmiddlewaretoken.value
        },
        body: JSON.stringify(postData)
    })

    let resData = await response.json()

    if(response){
        localStorage.setItem("token", resData.access) 
    }
})