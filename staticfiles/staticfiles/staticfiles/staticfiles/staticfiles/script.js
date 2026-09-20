const scrollElements = document.getElementsByClassName('scroll');
Array.from(scrollElements).forEach(element => {
    element.addEventListener('click', function (event) {
        event.preventDefault();
        document.querySelector('#about').scrollIntoView({
            behavior: "smooth"
        });
        document.querySelector('#my-works').scrollIntoView({
            behavior: "smooth"
        });

    })
})
const thumbnails = document.querySelectorAll('.thumbnail');
const overlay = document.getElementById('overlay');
const popBtn = document.getElementById('poppup-image');
const closeBtn = document.getElementById('close-btn');

thumbnails.forEach(thumbnail => {
    thumbnail.addEventListener('click', () => {
        const LargeImageSrc = thumbnail.src.replace('-thumbnail', '');
        popBtn.src = LargeImageSrc;
        overlay.style.display = 'flex';
    });

})
closeBtn.addEventListener('click', () => {
    overlay.style.display = 'none';
})
overlay.addEventListener('click', (e) => {
    if (e.target === overlay) { // Ensures only clicking outside the image closes the popup
        overlay.style.display = 'none';
    }
});

//silder pages
// Select all buttons and pages container
const navButtons = document.querySelectorAll('.navBtn');
const pages = document.querySelector('.pages');

// Add click event to each button
navButtons.forEach(button => {
    button.addEventListener('click', () => {
        navButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
        const targetPage = button.getAttribute('data-target');
        const targetIndex = Array.from(navButtons).findIndex(btn => btn.getAttribute('data-target') === targetPage);
        const offset = -targetIndex * 100; // Calculate offset based on page index
        pages.style.transform = `translateX(${offset}vw)`; // Slide to the page
    });
});
