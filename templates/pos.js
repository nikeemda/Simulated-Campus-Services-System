document.addEventListener('DOMContentLoaded', function() {
    // Function to handle PoS form submission
    document.getElementById('pos-sale-form').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent default form submission behavior
  
      // Get sale amount from the form input
      const saleAmount = parseFloat(document.getElementById('sale-amount').value);
  
      // Process the sale amount
      if (!isNaN(saleAmount) && saleAmount > 0) {
        // Sale amount is valid, display success message
        document.getElementById('pos-status').textContent = `Sale of $${saleAmount.toFixed(2)} completed successfully!`;
        document.getElementById('pos-status').classList.remove('error');
      } else {
        // Sale amount is invalid, display error message
        document.getElementById('pos-status').textContent = 'Invalid sale amount. Please enter a valid amount.';
        document.getElementById('pos-status').classList.add('error');
      }
    });
  });
  