const menuToggle = document.getElementById("nav-menu-toggle");
const mobileMenu = document.getElementById("nav-mobile-menu");

menuToggle.addEventListener("click", () => {
    if (mobileMenu.classList.contains("hidden")) {
        mobileMenu.classList.remove("hidden");
        setTimeout(() => {
            mobileMenu.classList.add("open");
        }, 10);
    } else {
        mobileMenu.classList.remove("open");
        setTimeout(() => {
            mobileMenu.classList.add("hidden");
        }, 300);
    }
});

// SCROLL-TO-TOP BUTTON
const scrollToTopButton = document.getElementById("scroll-to-top");

function toggleScrollToTopButton() {
    if (window.scrollY > 100) {
        scrollToTopButton.classList.remove("opacity-0", "pointer-events-none");
        scrollToTopButton.classList.add("opacity-100");
    } else {
        scrollToTopButton.classList.remove("opacity-100");
        scrollToTopButton.classList.add("opacity-0", "pointer-events-none");
    }
}

window.addEventListener("scroll", toggleScrollToTopButton);
