// Example JavaScript functionality

document.addEventListener('DOMContentLoaded', function() {
    // Example: Add confirmation for log out
    const logoutButton = document.querySelector('a[href*="logout"]');
    if (logoutButton) {
        logoutButton.addEventListener('click', function(event) {
            const confirmed = confirm("Are you sure you want to log out?");
            if (!confirmed) {
                event.preventDefault();
            }
        });
    }
});
