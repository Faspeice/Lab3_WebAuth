
document.getElementById('login-form').addEventListener('submit', function(e) {
    e.preventDefault();
    var formData = new FormData(this);

    fetch('/login', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('login-error').textContent = data.error;
        } else {
            window.location.href = '/base';
        }
    })
    .catch(error => console.error('Error:', error));
});


        function goToRegistration() {
            window.location.href = '/signup';
        }
