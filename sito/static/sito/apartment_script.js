// TOP SLIDESHOW
const CAROUSEL_CLICK_THRESHOLD = 5;

const carousel_parent = document.getElementById("image-carousel-container");
const carousel = document.getElementById("carousel-images");
const prev_btn = carousel_parent.querySelector('[data-role="prev-btn"]');
const next_btn = carousel_parent.querySelector('[data-role="next-btn"]');
const modal_btn = carousel_parent.querySelector('[data-role="modal-btn"]');
const image_width = carousel.querySelector("div").getBoundingClientRect().width;

prev_btn.addEventListener("click", (ev) => {
    carousel.scrollBy({ left: -image_width, behavior: "smooth" });
});

next_btn.addEventListener("click", (ev) => {
    carousel.scrollBy({ left: image_width, behavior: "smooth" });
});

let mouse_down = false;
let start_x, scroll_left;

const start_dragging = (e) => {
    mouse_down = true;
    start_x = e.pageX - carousel.offsetLeft;
    scroll_left = carousel.scrollLeft;
};

const stop_dragging = (e) => {
    mouse_down = false;
    const scroll = e.pageX - carousel.offsetLeft - start_x;
    if (Math.abs(scroll) <= CAROUSEL_CLICK_THRESHOLD) {
        open_modal();
    }
};

const move = (e) => {
    e.preventDefault();
    if (!mouse_down) {
        return;
    }
    const x = e.pageX - carousel.offsetLeft;
    const scroll = x - start_x;
    carousel.scrollLeft = scroll_left - scroll;
};

carousel.addEventListener("mousemove", move, false);
carousel.addEventListener("mousedown", start_dragging, false);
carousel.addEventListener("mouseup", stop_dragging, false);
carousel.addEventListener("mouseleave", stop_dragging, false);

// MODAL SLIDESHOW
const modal = document.getElementById("modal-overlay");
const everything = document.getElementById("everything");
const modal_container = document.getElementById("modal-container");
const modal_images = document.querySelectorAll('[data-group="modal-images"]');
const modal_total_images = modal_images.length;
const modal_prev_btn = document.getElementById("modal-prev-btn");
const modal_next_btn = document.getElementById("modal-next-btn");
let modal_current_image = 1;
let scroll_before_modal = 0;

function open_modal() {
    scroll_before_modal =
        document.documentElement.scrollTop || document.body.scrollTop;
    modal.classList.remove("hidden");
    document.getElementById("scroll-to-top").classList.add("hidden");
    everything.classList.add("hidden");
}

function close_modal() {
    modal.classList.add("hidden");
    document.getElementById("scroll-to-top").classList.remove("hidden");
    everything.classList.remove("hidden");
    window.scrollTo({ top: scroll_before_modal, left: 0, behavior: "instant" });
}

function modal_update_images() {
    modal_images.forEach((image, index) => {
        if (index + 1 === modal_current_image) {
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

modal_prev_btn.addEventListener("click", (ev) => {
    modal_current_image =
        modal_current_image === 1
            ? modal_total_images
            : modal_current_image - 1;
    modal_update_images();
});

modal_next_btn.addEventListener("click", (ev) => {
    modal_current_image =
        modal_current_image === modal_total_images
            ? 1
            : modal_current_image + 1;
    modal_update_images();
});

document.getElementById("modal-close-btn").addEventListener("click", (ev) => {
    close_modal();
});

modal_btn.addEventListener("click", (ev) => {
    open_modal();
});

document.addEventListener("keydown", (ev) => {
    if (modal.classList.contains("hidden")) {
        return;
    }
    if (event.key === "ArrowLeft") {
        modal_prev_btn.click();
    } else if (event.key === "ArrowRight") {
        modal_next_btn.click();
    } else if (event.key === 'Escape') {
        close_modal();
    }
});

modal_update_images();

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

// CLAMPED DESCRIPTION
const clamped_description = document.getElementById("clamped-description");
const read_more_btn = document.getElementById("descr-read-more");
const read_more_text = document.getElementById("read-more");
const read_less_text = document.getElementById("read-less");

function toggle_description_clamp() {
    if (clamped_description.classList.contains("expanded-text")) {
        clamped_description.classList.remove("expanded-text");
        clamped_description.classList.add("clamped-text");
        read_more_btn.innerHTML = `...${read_more_text.innerHTML}`;
    } else {
        clamped_description.classList.remove("clamped-text");
        clamped_description.classList.add("expanded-text");
        read_more_btn.innerHTML = `...${read_less_text.innerHTML}`;
    }
}

clamped_description.addEventListener("click", toggle_description_clamp);
read_more_btn.addEventListener("click", toggle_description_clamp);
