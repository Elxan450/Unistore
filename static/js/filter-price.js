const FilterLogicPrice = {
    url : `${location.origin}/api/products/`,

    filterProducts(price_gt, price_lt){
        let url = this.url

        if (price_gt && price_lt) {
            url += `?price__gt=${price_gt}&price__lt=${price_lt}`
        }

        fetch(url).then(response => response.json()).then(data => {
            
            document.getElementById("product-list").innerHTML = ''  


            for(let i in data){

                let fixed_price = data[i].price.toFixed(1);

                document.getElementById("product-list").innerHTML += `
                <div class="col-sm-6 col-md-4 product" data=${data[i].id}>
                <div class="body">
                  <a href="#favorites" class="favorites" data-favorite="inactive"><i class="ion-ios-heart-outline"></i></a>
                  <a href="product/${data[i].slug}/"><img src="${data[i].images[0].image}" alt=""/></a>

                  <div class="content">
                    <h1 class="h3">${data[i].product}</h1>

                    <p class="price">$${fixed_price}</p>
                      
                    <label>${data[i].category}</label>

                    <button class="btn btn-link"> <i class="ion-android-open"></i> Details</button>
                  </div>
                </div>
                </div>
                `
            }
        })
    }
}

let btn = document.getElementById("price-btn")
btn.addEventListener("click", function(event){
    event.preventDefault()
    let price_gt = Number(document.getElementById("price_gt").value)
    let price_lt = Number(document.getElementById("price_lt").value)
    FilterLogicPrice.filterProducts(price_gt, price_lt)
})
