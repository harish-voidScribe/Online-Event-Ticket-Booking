// OnlineBooking/static/OnlineBooking/js/index.js

document.addEventListener('DOMContentLoaded', function() {
  var amountInput = document.getElementById('amount');
  var ticketPrice = parseFloat("{{ ticket.price }}"); // Retrieve price per ticket from Django template

  // Optional: You can remove any event listeners related to quantitySelect if previously defined
});
