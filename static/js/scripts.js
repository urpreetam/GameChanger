// Add any interactivity you want here
// For example, you can add event listeners or animations

// Example: Change background color of image box on hover
document.querySelectorAll('.image-box').forEach(box => {
    box.addEventListener('mouseenter', () => {
        box.style.backgroundColor = '#e74c3c';
    });
    box.addEventListener('mouseleave', () => {
        box.style.backgroundColor = '#34495e';
    });
});
