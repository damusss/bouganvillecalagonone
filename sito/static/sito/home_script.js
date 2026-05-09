// APARTMENT SLIDESHOW
const SWIPE_THRESHOLD = 80;
const CLICK_THRESHOLD = 10;

document
    .querySelectorAll('[data-group="apartment-slideshows"]')
    .forEach((images_container) => {
        const prev_btn = images_container.querySelector(
            '[data-role="slideshow-prev"]',
        );
        const next_btn = images_container.querySelector(
            '[data-role="slideshow-next"]',
        );
        const link_btn = images_container.querySelector(
            '[data-role="slideshow-link"]',
        );
        const images_track = images_container.querySelector(
            '[data-role="slideshow-track"]',
        );
        const images = images_container.querySelectorAll(
            '[data-group="slideshow-images"]',
        );
        const total_images = images.length;

        let current_image = 1;
        let start_x = 0;
        let pointer_down = false;

        images_container.addEventListener("pointerdown", (e) => {
            if (e.target.closest("button")) {
                return;
            }

            pointer_down = true;
            start_x = e.clientX;
            images_container.setPointerCapture(e.pointerId);
            images_track.style.transition = "none";
        });

        images_container.addEventListener("pointermove", (e) => {
            if (!pointer_down) return;

            const current_x = e.clientX;
            const delta_x = current_x - start_x;

            images_track.style.transform = `translateX(${delta_x}px)`;

            if (Math.abs(delta_x) > SWIPE_THRESHOLD) {
                pointer_down = false;

                images_track.style.transition = "transform 0.3s ease-out";
                images_track.style.transform = "translateX(0px)";

                images_container.releasePointerCapture(e.pointerId);

                if (delta_x > 0) {
                    prev_btn.click();
                } else {
                    next_btn.click();
                }
            }
        });

        images_container.addEventListener("pointerup", (e) => {
            if (!pointer_down) return;
            pointer_down = false;

            const current_x = e.clientX;
            const delta_x = current_x - start_x;

            images_track.style.transition = "transform 0.3s ease-out";
            images_track.style.transform = "translateX(0px)";

            if (Math.abs(delta_x) < CLICK_THRESHOLD) {
                link_btn.click();
            }
        });

        images_container.addEventListener("pointercancel", (e) => {
            pointer_down = false;
            images_track.style.transition = "transform 0.3s ease-out";
            images_track.style.transform = "translateX(0px)";
            images_container.releasePointerCapture(e.pointerId);
        });

        images_container.addEventListener("dragstart", (e) => {
            e.preventDefault();
        });

        function update_images() {
            images.forEach((image, index) => {
                if (index + 1 === current_image) {
                    image.classList.remove("opacity-0");
                    image.classList.add("opacity-100");
                    image.classList.remove("hidden");
                } else {
                    image.classList.remove("opacity-100");
                    image.classList.add("opacity-0");
                    image.classList.add("hidden");
                }
            });
        }

        const prev_move_images = function () {
            current_image =
                current_image === 1 ? total_images : current_image - 1;
            update_images();
        };
        prev_btn.addEventListener("click", prev_move_images);

        const next_move_images = function () {
            current_image =
                current_image === total_images ? 1 : current_image + 1;
            update_images();
        };
        next_btn.addEventListener("click", next_move_images);

        update_images();
    });

// PANORAMA SLIDESHOWS
let skip = false;
let current_slide = 1;

const slides_cont = document.getElementById("slides-container");
const slides_cont_desktop = document.getElementById("slides-container-desktop");

const slides = document.querySelectorAll('[data-group="slides"]');
const slides_prev = document.querySelectorAll('[data-group="slides-prev"]');
const slides_next = document.querySelectorAll('[data-group="slides-next"]');

const slides_desktop = document.querySelectorAll(
    '[data-group="slides-desktop"]',
);
const slides_prev_desktop = document.querySelectorAll(
    '[data-group="slides-prev-desktop"]',
);
const slides_next_desktop = document.querySelectorAll(
    '[data-group="slides-next-desktop"]',
);

const slides_slides = [
    slides,
    slides_desktop,
    slides_prev,
    slides_prev_desktop,
    slides_next,
    slides_next_desktop,
];
const total_slides = slides.length || slides_desktop.length;

function update_slides() {
    slides_slides.forEach((slides_s, sI) => {
        slides_s.forEach((slide, index) => {
            if (index + 1 === current_slide) {
                slide.classList.remove("opacity-0");
                slide.classList.add("opacity-100");
            } else {
                slide.classList.remove("opacity-100");
                slide.classList.add("opacity-0");
            }
        });
    });
}

const s_prev_btn = document.getElementById("prev-btn");
const s_next_btn = document.getElementById("next-btn");
const s_prev_btn_desktop = document.getElementById("prev-btn-desktop");
const s_next_btn_desktop = document.getElementById("next-btn-desktop");

s_prev_btn.addEventListener("click", function () {
    current_slide = current_slide === 1 ? total_slides : current_slide - 1;
    skip = true;
    update_slides();
});

s_next_btn.addEventListener("click", function () {
    current_slide = current_slide === total_slides ? 1 : current_slide + 1;
    skip = true;
    update_slides();
});

s_prev_btn_desktop.addEventListener("click", function () {
    current_slide = current_slide === 1 ? total_slides : current_slide - 1;
    skip = true;
    update_slides();
});

s_next_btn_desktop.addEventListener("click", function () {
    current_slide = current_slide === total_slides ? 1 : current_slide + 1;
    skip = true;
    update_slides();
});

setInterval(() => {
    if (skip) {
        skip = false;
        return;
    }
    current_slide = current_slide === total_slides ? 1 : current_slide + 1;
    update_slides();
}, 3000);

update_slides();

// PANORAMA DRAG
[
    [slides_cont, s_prev_btn, s_next_btn],
    [slides_cont_desktop, s_prev_btn_desktop, s_next_btn_desktop],
].forEach((slide_data) => {
    const slide_cont = slide_data[0];
    const slide_prev_btn = slide_data[1];
    const slide_next_btn = slide_data[2];
    let slide_start_x = 0;
    let slide_pointer_down = false;
    const images_track = slide_cont.querySelector('[data-role="slides-track"]');

    slide_cont.addEventListener("pointerdown", (e) => {
        if (e.target.closest("button")) {
            return;
        }
        slide_pointer_down = true;
        slide_start_x = e.clientX;
        slide_cont.setPointerCapture(e.pointerId);
        images_track.style.transition = "none";
    });

    slide_cont.addEventListener("pointermove", (e) => {
        if (!slide_pointer_down) return;

        const current_x = e.clientX;
        const delta_x = current_x - slide_start_x;

        images_track.style.transform = `translateX(${delta_x}px)`;

        if (Math.abs(delta_x) > SWIPE_THRESHOLD) {
            slide_pointer_down = false;

            images_track.style.transition = "transform 0.3s ease-out";
            images_track.style.transform = "translateX(0px)";

            slide_cont.releasePointerCapture(e.pointerId);

            if (delta_x > 0) {
                slide_prev_btn.click();
            } else {
                slide_next_btn.click();
            }
        }
    });

    slide_cont.addEventListener("pointerup", (e) => {
        if (!slide_pointer_down) return;
        slide_pointer_down = false;

        const current_x = e.clientX;
        const delta_x = current_x - slide_start_x;

        images_track.style.transition = "transform 0.3s ease-out";
        images_track.style.transform = "translateX(0px)";
    });

    slide_cont.addEventListener("pointercancel", (e) => {
        slide_pointer_down = false;
        images_track.style.transition = "transform 0.3s ease-out";
        images_track.style.transform = "translateX(0px)";
        slide_cont.releasePointerCapture(e.pointerId);
    });

    slide_cont.addEventListener("dragstart", (e) => {
        e.preventDefault();
    });
});

// APARTMENT SWAP
const apartment_cont = document.getElementById("apartment-grid-2");
const first_child = apartment_cont.children[0];
const second_child = apartment_cont.children[1];

function swap_for_large_devices() {
    if (window.matchMedia("(min-width: 1024px)").matches) {
        apartment_cont.insertBefore(second_child, first_child);
    } else {
        apartment_cont.insertBefore(first_child, second_child);
    }
}

swap_for_large_devices();
window.addEventListener("resize", swap_for_large_devices);
