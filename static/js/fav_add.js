let btn = document.getElementById("fav_add")
btn.addEventListener("click", async function(event){
    event.preventDefault()
    postData = {
        "favorite_list" : btn.getAttribute("data"),
        "product" : btn.getAttribute("value")
    }   

    url = `http://localhost:8000/api/favorites/`
    fetch(url, {
        method : "POST",
        headers : {
            "Content-Type" : "application/json",
        },
        body : JSON.stringify(postData)
    })
    .then(response => {
        if (response.ok){
            btn.setAttribute("id", "fav_delete")
            btn.setAttribute("data", postData.favorite_list)
            btn.setAttribute("value", postData.product)
            btn.innerHTML = `
                <i class="ion-ios-heart"></i> Delete from the wishlist 
            `
            window.alert("Added successfully!")
        }

        else{
            window.alert("Already in the wishlist")
        }
    })
})
