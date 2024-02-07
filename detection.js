var selectedImage = document.getElementById('selectedImage');
var selectedImageBox = document.getElementById('selectedImageBox');
var fileInput = document.getElementById('imageFile');
var resultsContainer = document.getElementById('resultsContainer');
var spinner = document.getElementById('spinner');

fileInput.addEventListener('change', function () {
    if (fileInput.files.length > 0) {
        selectedImage.style.width = '300px'; // Replace '300px' with your desired width
        selectedImage.style.height = '200px';
        selectedImage.style.display = 'block';
        var reader = new FileReader();

        reader.onload = function (e) {
            selectedImage.src = e.target.result;

        };
        reader.readAsDataURL(fileInput.files[0]);
        // Show the selected image and hide the file input
        selectedImageBox.style.display = 'block';
        fileInput.style.display = 'none';
    } else {
        // Hide the selected image and show the file input
        selectedImageBox.style.display = 'none';
        fileInput.style.display = 'block';
        selectedImage.src = ''; // Clear the image source
    }
});

function uploadImage() {
    var form = document.getElementById("imageUploadForm");
    var formData = new FormData(form);

    // Fetch CSRF token from the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

    // Include CSRF token in the headers
    $.ajax({
        type: 'POST',
        url: '/upload_image/',  // Replace with your actual endpoint
        data: formData,
        contentType: false,
        processData: false,
        beforeSend: function (xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrfToken);
            $('#uploadButton').prop('disabled', true);
            resultsContainer.innerHTML = '';
            // Show the spinner
            spinner.style.display = 'inline-block';


        },
        success: function (result) {
            console.log('Image upload response:', result);
            // Handle the response as needed
            displayResults(result.data);
            fileInput.style.display = 'block';
            spinner.style.display = 'none';
        },
        error: function (error) {
            console.error('Error uploading image:', error);
        },
        complete: function () {
            document.getElementById('uploadButton').disabled = false;
            // Hide the selected image and show the file input
            fileInput.style.display = 'block';
            spinner.style.display = 'none';
        }
    });
}

function displayResults(data) {
    // Create a container for the results
    resultsContainer.innerHTML = '';
    const model1 = data.model_1

    // Create a div for each model's results
    var modelDiv = document.createElement('div');
    modelDiv.className = 'model-results';
    var modelNameLabel = document.createElement('p');
    modelNameLabel.className = 'result-label';
    modelNameLabel.textContent = 'Predicted Results';
    modelDiv.appendChild(modelNameLabel);

    // Add score and class information
    var scoreLabel = document.createElement('p');
    scoreLabel.innerHTML = 'Plant: <span class="label-text">' + model1.plant + '</span>';
    modelDiv.appendChild(scoreLabel);

    var classLabel = document.createElement('p');
    classLabel.innerHTML = 'Disease: <span class="label-text">' + model1.disease + '</span>';
    modelDiv.appendChild(classLabel);

    // Append the model div to the results container
    resultsContainer.appendChild(modelDiv);
    modelDiv.scrollIntoView({ behavior: 'smooth', block: 'end' });

}



