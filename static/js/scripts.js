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

// For gameplay.html video handling
window.onload = function() {
    const videoContainer = document.getElementById('start-video-container');
    const video = document.getElementById('start-video');

    videoContainer.style.display = 'flex';
    video.play();

    video.onended = function() {
        videoContainer.style.display = 'none';
        document.getElementById('game-content').style.display = 'block';
        startGame();
    };
};

function startGame() {
    // Game initialization logic here
}
