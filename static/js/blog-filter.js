function extractFirst50Words(text) {
  // Split the text into words using spaces as the delimiter
  const words = text.split(' ');

  // Take the first 50 words (or fewer if the text has fewer than 50 words)
  const first50Words = words.slice(0, 50);

  // Join the first 50 words back together with spaces
  const result = first50Words.join(' ');

  return result;
}

function extractFirst10Characters(text) {
  // Use array slicing to extract the first 10 characters
  const first10Characters = text.slice(0, 10);

  return first10Characters;
}


document.getElementById("ordering").addEventListener("click", function(event){
    event.preventDefault()
    let url = `${location.origin}/api/blogs/?ordering=title&page=1`
    fetch(url).then(response => response.json()).then(data => {
            
        document.getElementById("blogs").innerHTML = ''

        for(let i in data){
            document.getElementById("blogs").innerHTML += 
            `   
            <div class="col-sm-6 col-md-6 item">
            <div class="body">
              <a href="${data[i].slug}/" class="view"><i class="ion-ios-book-outline"></i></a>

              <a href="${data[i].slug}/">
                <img src="${data[i].image}" title="Apple Devices" alt="Apple Devices">
              </a>

              <div class="caption">
                <h1 class="h3">${data[i].title}</h1>
                <label>${extractFirst10Characters(data[i].created_at)}</label>
                <hr class="offset-sm">

                <p>
                  ${extractFirst50Words(data[i].description)}
                </p>
                <hr class="offset-sm">

                <a href="${data[i].slug}/"> View article <i class="ion-ios-arrow-right"></i> </a>
              </div>
            </div>
          </div>

            `
        }
        
    })
})


document.getElementById("-ordering").addEventListener("click", function(event){
    event.preventDefault()
    let url = `${location.origin}/api/blogs/?ordering=-title`
    fetch(url).then(response => response.json()).then(data => {
            
        document.getElementById("blogs").innerHTML = ''

        for(let i in data){
            document.getElementById("blogs").innerHTML += 
            `   
            <div class="col-sm-6 col-md-6 item">
            <div class="body">
              <a href="${data[i].slug}/" class="view"><i class="ion-ios-book-outline"></i></a>

              <a href="${data[i].slug}/">
                <img src="${data[i].image}" title="Apple Devices" alt="Apple Devices">
              </a>

              <div class="caption">
                <h1 class="h3">${data[i].title}</h1>
                <label>${extractFirst10Characters(data[i].created_at)}</label>
                <hr class="offset-sm">

                <p>
                  ${extractFirst50Words(data[i].description)}
                </p>
                <hr class="offset-sm">

                <a href="${data[i].slug}/"> View article <i class="ion-ios-arrow-right"></i> </a>
              </div>
            </div>
          </div>

            `
        }
        
    })
})