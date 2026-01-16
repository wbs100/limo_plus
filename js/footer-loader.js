document.addEventListener("DOMContentLoaded", function () {
    fetch('footer-content.html?v=' + Date.now())
        .then(response => response.text())
        .then(data => {
            const footerContainer = document.querySelector('.footer');
            if (footerContainer) {
                footerContainer.innerHTML = data;
            }
        })
        .catch(error => console.error('Error loading footer:', error));
});
