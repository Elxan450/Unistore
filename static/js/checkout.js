const countryInput = document.getElementById('country');
const listItems = document.querySelectorAll('.countries');

// Add click event listeners to each list item
listItems.forEach((item) => {
item.addEventListener('click', () => {
	// Update the input field value with the selected country
	let pk = item.getAttribute('value');
	let url = `${location.origin}/api/cities/?country=${pk}`
	fetch(url).then(response => response.json()).then(data => {
            
		document.getElementById("city").value = ""
		document.getElementById("city-drop").innerHTML = ''  


		for(let i in data){
			console.log(data[i].name)
			document.getElementById("city-drop").innerHTML += `
				<li data-value="${data[i].name}" class="cities">${data[i].name}</li>
			`
		}
	})
	});
});