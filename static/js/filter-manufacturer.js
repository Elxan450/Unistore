const FilterLogicManufacturer = {
    url : `${location.origin}/api/products/`,

    filterProducts(manufacturer){
        let url = this.url

        if (manufacturer) {
            url += `?manufacturer=${manufacturer}`
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

let changed = document.getElementById("product-list").getAttribute("data")
console.log(changed)

let productManufacturer = document.getElementsByClassName("manufacturer-filter")

for(let k = 0; productManufacturer.length; k++){
    productManufacturer[k].addEventListener("click", function(event){
        event.preventDefault()
        const manufacturer = this.getAttribute("data")
        FilterLogicManufacturer.filterProducts(manufacturer)
    })
} 
