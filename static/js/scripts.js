// Add any interactivity you want here
// For example, you can add event listeners or animations

// Example: Change background color of image box on hover
// Add click event listeners to each box
document.querySelectorAll('.image-box').forEach((box, index) => {
    box.addEventListener('mouseenter', () => {
        box.style.backgroundColor = '#e74c3c';
    });
    box.addEventListener('mouseleave', () => {
        box.style.backgroundColor = '#34495e';
    });

    // Click event listener with dynamic routing based on box index
    box.addEventListener('click', () => {
        // Redirect to the game page with the box index (1-based)
        window.location.href = `/game/${index + 1}`;
    });
});

