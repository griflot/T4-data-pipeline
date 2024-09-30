document.getElementById('gradeForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form from submitting the traditional way

    const name = document.getElementById('name').value;
    const grade = document.getElementById('grade').value;

    // Prepare the message in JSON format
    const jsonMessage = JSON.stringify({ name: name, grade: grade });

    // Send the data to Kafka
    fetch('http://localhost:5000/send', { // Update to your server endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: jsonMessage
    })
    .then(response => {
        if (response.ok) {
            document.getElementById('message').innerText = 'Data sent successfully!';
        } else {
            document.getElementById('message').innerText = 'Error sending data.';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('message').innerText = 'Error sending data.';
    });
});
