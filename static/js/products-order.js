const FilterLogicOrdering = {
    url : `${location.origin}/api/products/`,

    filterProducts(ordering){
        let url = this.url

        if (price_gt && price_lt) {
            url += `?ordering=${ordering}`
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
                    <button class="btn btn-primary btn-sm rounded"> <i class="ion-bag"></i> Add to cart</button>
                  </div>
                </div>
                </div>
                `
            }
        })
    }
}

let order_types = document.getElementsByClassName("ordering")

for(let i = 0; order_types.length; i++){
    order_types[i].addEventListener("click", function(event){
        event.preventDefault()
        const ordering = this.getAttribute("data")
        FilterLogicOrdering.filterProducts(ordering)
    })
}