const FilterLogicCategory = {
    url : `${location.origin}/api/products_common/`,

    filterProducts(category){
        let url = this.url

        if (category) {
            url += `?category=${category}`
        }

        fetch(url).then(response => response.json()).then(data => {
            
            document.getElementById("product-list").innerHTML = ''

            for(let i in data){

                for(let product_version in data[i].product_versions){
                    
                let fixed_price = data[i].product_versions[product_version].price.toFixed(1);

                document.getElementById("product-list").innerHTML += `
                <div class="col-sm-6 col-md-4 product" data=${data[i].product_versions[product_version].id}>
                <div class="body">
                  <a href="#favorites" class="favorites" data-favorite="inactive"><i class="ion-ios-heart-outline"></i></a>
                  <a href="product/${data[i].product_versions[product_version].slug}/"><img src="${data[i].product_versions[product_version].images[0].image}" alt=""/></a>

                  <div class="content">
                    <h1 class="h3">${data[i].product_versions[product_version].product}</h1>

                    <p class="price">$${fixed_price}</p>
                      
                    <label>${data[i].product_versions[product_version].category}</label>

                    <button class="btn btn-link"> <i class="ion-android-open"></i> Details</button>
                  </div>
                </div>
                </div>
                `
                }
            }
        })
    }
}


let productCategory = document.getElementsByClassName("category-filter")

for(let i = 0; productCategory.length; i++){
    productCategory[i].addEventListener("click", function(event){
        event.preventDefault()
        const category = this.getAttribute("data")
        FilterLogicCategory.filterProducts(category )
    })
}



