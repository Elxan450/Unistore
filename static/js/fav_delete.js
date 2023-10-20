let btn_delete = document.getElementById("fav_delete")
btn_delete.addEventListener("click", async function(event){
    event.preventDefault()
    let favorite_list = btn_delete.getAttribute("data")
    let product = btn_delete.getAttribute("value")

    const url = `http://localhost:8000/api/favorites/?favorite_list=${favorite_list}&product=${product}`
    const response = await fetch(url);
    var data = await response.json();
    var id = data[0].id

    const url_2 = `http://localhost:8000/api/favorite/${id}/`
    
    fetch(url_2, {
        method : 'DELETE',
    })
    .then(response => {
        if (response.ok){
            btn_delete.setAttribute("id", "fav_delete")
            btn_delete.setAttribute("data", favorite_list)
            btn_delete.setAttribute("value", product)
            btn_delete.innerHTML = `
                <i class="ion-ios-heart"></i> See later
            `
            window.alert("Removed successfully!")
        }

        else{
            window.alert("Already removed!")
        }
    })
})

