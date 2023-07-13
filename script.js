document.getElementById('eventForm').addEventListener('submit', function(e) {
    e.preventDefault();

    var eventText = document.getElementById('eventText').value;

    // Send the event text to the backend for processing
    fetch('/create_event', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'eventText': eventText })
    })
    .then(function(response) {
        if (response.ok) {
            return response.text();
        }
        throw new Error('Network response was not ok.');
    })
    .then(function(responseText) {
        alert(responseText);
    })
    .catch(function(error) {
        console.log('Error:', error.message);
    });
});
