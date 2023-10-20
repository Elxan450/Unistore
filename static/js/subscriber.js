let newsletterForm = document.getElementById("newsletter-form")
newsletterForm.addEventListener("submit", async function(event){
    event.preventDefault()
    postData = {
        "email" : newsletterForm.email.value
    }

    fetch(`${location.origin}/api/newsletters/`, {
        method : "POST",
        headers : {
            "Content-Type" : "application/json",
            "X-CSRFToken" : newsletterForm.csrfmiddlewaretoken.value
        },
        body : JSON.stringify(postData)
    })
    .then(response => {
        if (response.ok){
            newsletterForm.innerHTML = "Thanks for your subscription!"
        }

        else{
            window.alert("newsletter with this Email already exists!")
        }
    })
})