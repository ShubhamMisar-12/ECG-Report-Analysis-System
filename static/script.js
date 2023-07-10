var form = document.getElementById('emotion-form');
var fileInput = document.getElementById('image');

// Add event listener to the form submission
form.addEventListener('submit', function(event) {
  if (!fileInput.value) {
    event.preventDefault(); // Prevent form submission if no file is selected
    alert('Please select a file to upload.');
  }
});
