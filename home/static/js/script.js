const header = document.querySelector('header');
window.addEventListener('scroll', () => {
    if (window.scrollY > 0) {
        header.classList.add('scrolled');
    }
    else {
        header.classList.remove('scrolled');
    }
});
document.addEventListener("DOMContentLoaded", () => {
    const odometers = document.querySelectorAll(".odometer");
    const animateOdometer = (odometer) => {
        const target = +odometer.getAttribute("data-target");
        const speed = 80; // Adjust speed as required
        const increment = target / speed;

        let value = 0;
        const updateCounter = () => {
        value += increment;
        if (value >= target) {
            odometer.textContent = target;
        }
        else {
            odometer.textContent = Math.floor(value);
            requestAnimationFrame(updateCounter);
            }
        };
        updateCounter();
    };
    const startOdometerAnimation = () => {
        odometers.forEach((odometer) => {
        const rect = odometer.getBoundingClientRect();
        if (rect.top >= 0 && rect.bottom <= window.innerHeight) {
            if (!odometer.classList.contains("animated")) {
            odometer.classList.add("animated");
            animateOdometer(odometer);
            }
        }
        });
    };
    window.addEventListener("scroll", startOdometerAnimation);
    startOdometerAnimation(); // Trigger on page load
    });
// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", () => {
    const notification = document.getElementById("notification");
    setTimeout(() => {
        notification.style.display = "none";
    }, 5000);
});
