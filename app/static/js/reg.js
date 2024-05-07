
document.getElementById('signup-form').addEventListener('submit', function(e) {
    e.preventDefault();
    var formData = new FormData(this);

    fetch('/signup', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('signup-error').textContent = data.error;
        } else {
            window.location.href = '/login';
        }
    })
    .catch(error => console.error('Error:', error));
});


        function goToLogin() {
            window.location.href = '/login';
        }