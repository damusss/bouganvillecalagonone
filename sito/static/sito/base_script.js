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

// FORM RULES IF IT EXISTS
document.addEventListener("DOMContentLoaded", function () {
    const checkin = document.getElementById("start-date");
    const checkout = document.getElementById("end-date");

    if (checkin != null && checkout != null) {

        function addDaysToString(dateString, daysToAdd) {
            const parts = dateString.split("-");
            const dateObj = new Date(parts[0], parts[1] - 1, parts[2]);

            dateObj.setDate(dateObj.getDate() + daysToAdd);

            const year = dateObj.getFullYear();
            const month = String(dateObj.getMonth() + 1).padStart(2, "0");
            const day = String(dateObj.getDate()).padStart(2, "0");

            return `${year}-${month}-${day}`;
        }

        const now = new Date();
        const currentYear = now.getFullYear();
        const currentMonth = String(now.getMonth() + 1).padStart(2, "0");
        const currentDay = String(now.getDate()).padStart(2, "0");
        const today = `${currentYear}-${currentMonth}-${currentDay}`;

        const defaultCheckoutMin = addDaysToString(today, 7);
        checkin.min = today;
        checkout.min = defaultCheckoutMin;

        checkin.addEventListener("change", function (event) {
            const selected_date = event.target.value;

            if (selected_date) {
                checkout.min = addDaysToString(selected_date, 7);
            } else {
                checkout.min = defaultCheckoutMin;
            }

            if (checkout.value && checkout.value < checkout.min) {
                checkout.value = "";
            }
        });
    }
});