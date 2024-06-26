document.addEventListener('DOMContentLoaded', function() {
    // Function to handle NFC input
    function handleNFCInput() {
      // Simulating NFC input
      // Replace this with actual NFC input handling logic
      const nfcData = {
        username: 'example_user',
        password: 'example_password',
        isValid: true // Assuming the input is valid for demonstration
      };
  
      // Update status message based on NFC input validity
      const statusMessage = document.getElementById('door-access-status');
      if (nfcData.isValid) {
        statusMessage.textContent = 'Door opened successfully!';
        statusMessage.classList.remove('error');
      } else {
        statusMessage.textContent = 'Invalid NFC input. Access denied.';
        statusMessage.classList.add('error');
      }
    }
  
    // Call handleNFCInput function when the page is loaded
    handleNFCInput();
  });
  