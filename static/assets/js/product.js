document.querySelectorAll('.icon-btn').forEach(button => {
    button.addEventListener('click', function(event) {
        event.preventDefault();
        // Perform AJAX request to update the wishlist status
        // On success:
        let icon = this.querySelector('i');
        if (icon.classList.contains('fal')) {
            icon.classList.remove('fal');
            icon.classList.add('fa-solid');
            icon.style.color = '#f70202';
        } else {
            icon.classList.remove('fa-solid');
            icon.classList.add('fal');
            icon.style.color = '';
        }
    });
});
