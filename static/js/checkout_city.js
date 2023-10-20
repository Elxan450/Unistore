const cityInput = document.getElementById('city');
const cityListItems = document.querySelectorAll('.cities');

// Add click event listeners to each city list item
cityListItems.forEach((item) => {
  item.addEventListener('click', () => {
	// Update the input field value with the selected city
	cityInput.value = item.getAttribute('data-value');
  });
});