function loadingMessage() {
    document.getElementById('loading-message').style.display = 'block';
    document.getElementById('search-form-container').style.display = 'none';
    var errorMessage = document.getElementById('error-message');
    if (errorMessage) {
        errorMessage.style.display = 'none';
    }
}