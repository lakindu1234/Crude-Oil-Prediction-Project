document.getElementById('predictBtn').addEventListener('click', predictPrice);

function predictPrice() {
    const year = document.getElementById('year').value;
    const month = document.getElementById('month').value;

    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ year: parseInt(year), month: parseInt(month) }),
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.predicted_price !== undefined) {
                document.getElementById(
                    'result'
                ).innerText = `Predicted Price: $${data.predicted_price.toFixed(2)}`;
            } else {
                document.getElementById('result').innerText =
                    'Error: ' + (data.error || 'Unknown error');
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            document.getElementById('result').innerText = 'Server error. Please try again later.';
        });
}
