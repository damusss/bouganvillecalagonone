const menu_toggle = document.getElementById("nav-menu-toggle");
const mobile_menu = document.getElementById("nav-mobile-menu");

menu_toggle.addEventListener("click", () => {
    if (mobile_menu.classList.contains("hidden")) {
        mobile_menu.classList.remove("hidden");
        setTimeout(() => {
            mobile_menu.classList.add("open");
        }, 10);
    } else {
        mobile_menu.classList.remove("open");
        setTimeout(() => {
            mobile_menu.classList.add("hidden");
        }, 300);
    }
});

// SCROLL-TO-TOP BUTTON
const scroll_to_top_btn = document.getElementById("scroll-to-top");

function toggle_scroll_to_top_btn() {
    if (window.scrollY > 100) {
        scroll_to_top_btn.classList.remove("opacity-0", "pointer-events-none");
        scroll_to_top_btn.classList.add("opacity-100");
    } else {
        scroll_to_top_btn.classList.remove("opacity-100");
        scroll_to_top_btn.classList.add("opacity-0", "pointer-events-none");
    }
}

window.addEventListener("scroll", toggle_scroll_to_top_btn);
