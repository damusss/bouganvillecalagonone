const injector = document.getElementById("map-injector");

function injectGoogleMapIFrame() {
    if (document.cookie.split("; ").includes("gmaps_consent=accepted")) {
        injector.innerHTML =
            '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4153.993020868887!2d9.625948581771791!3d40.28568967254134!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12def42637a344d7%3A0x8114c1df60c1be9c!2sLa%20Bouganville%20Apartments!5e1!3m2!1sen!2sit!4v1777996488921!5m2!1sen!2sit" class="w-full aspect-square md:aspect-video rounded-md mb-6" style="border: 0" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" ></iframe>';
    }
}

function acceptAndViewMap() {
    if (!document.cookie.split("; ").includes("gmaps_consent=accepted")) {
        const maxAgeSeconds = 180 * 24 * 60 * 60;
        document.cookie = `gmaps_consent=accepted; max-age=${maxAgeSeconds}; path=/; SameSite=Strict; Secure`;
        injectGoogleMapIFrame();
    }
}

injectGoogleMapIFrame();

document
    .querySelectorAll('[data-group="images-main-cont"]')
    .forEach((images_main_cont) => {
        const images_cont = images_main_cont.querySelector(
            '[data-cont="images"',
        );
        const firstImage = images_cont.querySelector("div");
        let imageWidth;
        if (firstImage) {
            imageWidth = firstImage.scrollWidth;
        } else {
            imageWidth = 0;
        }
        images_main_cont
            .querySelector('[data-role="left"]')
            .addEventListener("click", (ev) => {
                images_cont.scrollBy({
                    left: -1 * imageWidth,
                    behavior: "smooth",
                });
            });
        images_main_cont
            .querySelector('[data-role="right"]')
            .addEventListener("click", (ev) => {
                images_cont.scrollBy({
                    left: 1 * imageWidth,
                    behavior: "smooth",
                });
            });

        let mouseDown = false;
        let startX, scrollLeft;

        const startDragging = (e) => {
            mouseDown = true;
            startX = e.pageX - images_cont.offsetLeft;
            scrollLeft = images_cont.scrollLeft;
        };

        const stopDragging = (e) => {
            mouseDown = false;
        };

        const move = (e) => {
            e.preventDefault();
            if (!mouseDown) {
                return;
            }
            const x = e.pageX - images_cont.offsetLeft;
            const scroll = x - startX;
            images_cont.scrollLeft = scrollLeft - scroll;
        };

        images_cont.addEventListener("mousemove", move, false);
        images_cont.addEventListener("mousedown", startDragging, false);
        images_cont.addEventListener("mouseup", stopDragging, false);
        images_cont.addEventListener("mousecancel", stopDragging, false);
        images_cont.addEventListener("mouseleave", stopDragging, false);
    });
