
const folderInput = document.getElementById("folderInput");
const submitBtn = document.getElementById('submitBtn');
const virusDetectedMessage = document.getElementById('virus-detected-message');

submitBtn.addEventListener('click', () => {
  const files = fileInput.files;

  if (files.length === 0) {
    alert('Please select a folder.');
    return;
  }

  const formData = new FormData();

  for (let i = 0; i < files.length; i++) {
    formData.append('file[]', files[i]);
  }

  fetch("/index", {
    method: "POST",
    body: formData,
  })


    .then(response => {
      if (response.ok) {
        // Files uploaded successfully, now scan for viruses
        const folderPath = '/path/to/folder';

        // Code to scan folder for viruses goes here...
        const virusDetected = true; // Set to true if a virus is detected

        if (virusDetected) {
          virusDetectedMessage.textContent = 'Virus detected!';
          virusDetectedMessage.style.color = 'red';
          virusDetectedMessage.style.fontWeight = 'bold';
        }
        else {
          virusDetectedMessage.textContent = '';
        }

        alert('Files uploaded successfully.');
      }
      else {
        alert('Error uploading files.');
      }
    })
    .catch(error => {
      console.error(error);
    });
});
