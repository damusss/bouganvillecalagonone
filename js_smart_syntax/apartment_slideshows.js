// AID->APARTM_VARIABLE.index
// <>{% for APARTM_VARIABLE in apartments %}
// <>{% if APARTM_VARIABLE.available == True %}

let currentImageAID = 1;
var totalImagesAID = 0;
var imagesAID = [];
// <>{% for image in APARTM_VARIABLE.images %}
totalImagesAID += 1;
imagesAID.push(document.getElementById("image-AID-{{forloop.counter0}}"));
// <>{% endfor %}

const imagesContainerAID = document.getElementById("slideshow-apartment-AID");
const imagesTrackAID = document.getElementById("slideshow-a-AID");
const prevBtnAID = document.getElementById("prevBtn-AID");
const nextBtnAID = document.getElementById("nextBtn-AID");

let startXAID = 0;
let isPointerDownAID = false;

const SWIPE_THRESHOLD_AID = 100;

imagesContainerAID.addEventListener("pointerdown", (e) => {
    if (e.target.closest("button")) {
        return;
    }

    isPointerDownAID = true;
    startXAID = e.clientX;
    imagesContainerAID.setPointerCapture(e.pointerId);
    imagesTrackAID.style.transition = "none";
});

imagesContainerAID.addEventListener("pointermove", (e) => {
    if (!isPointerDownAID) return;

    const currentX = e.clientX;
    const deltaX = currentX - startXAID;

    imagesTrackAID.style.transform = `translateX(${deltaX}px)`;

    if (Math.abs(deltaX) > SWIPE_THRESHOLD_AID) {
        isPointerDownAID = false;

        imagesTrackAID.style.transition = "transform 0.3s ease-out";
        imagesTrackAID.style.transform = "translateX(0px)";

        imagesContainerAID.releasePointerCapture(e.pointerId);

        if (deltaX > 0) {
            prevBtnAID.click();
        } else {
            nextBtnAID.click();
        }
    }
});

imagesContainerAID.addEventListener("pointerup", (e) => {
    if (!isPointerDownAID) return;
    isPointerDownAID = false;

    const currentX = e.clientX;
    const deltaX = currentX - startXAID;

    if (Math.abs(deltaX) < SWIPE_THRESHOLD_AID) {
        imagesTrackAID.style.transition = "transform 0.3s ease-out";
        imagesTrackAID.style.transform = "translateX(0px)";

        document.getElementById("slideshow-link-AID").click();
    }
});

imagesContainerAID.addEventListener("pointercancel", (e) => {
    isPointerDownAID = false;
    imagesTrackAID.style.transition = "transform 0.3s ease-out";
    imagesTrackAID.style.transform = "translateX(0px)";
    imagesContainerAID.releasePointerCapture(e.pointerId);
});

imagesContainerAID.addEventListener("dragstart", (e) => {
    e.preventDefault();
});

function updateImagesAID() {
    imagesAID.forEach((image, index) => {
        if (index + 1 === currentImageAID) {
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

const prevMoveImagesAID = function () {
    currentImageAID =
        currentImageAID === 1 ? totalImagesAID : currentImageAID - 1;
    updateImagesAID();
    // <>{%if APARTM_VARIABLE.index == apartment.index %}
    if (isApartment && modal.classList.contains("hidden")) {
        prevMoveImagesM();
    }
    // <>{%endif%}
};
prevBtnAID.addEventListener("click", prevMoveImagesAID);

const nextMoveImagesAID = function () {
    currentImageAID =
        currentImageAID === totalImagesAID ? 1 : currentImageAID + 1;
    updateImagesAID();
    // <>{%if APARTM_VARIABLE.index == apartment.index %}
    if (isApartment && modal.classList.contains("hidden")) {
        nextMoveImagesM();
    }
    // <>{%endif%}
};
nextBtnAID.addEventListener("click", nextMoveImagesAID);

updateImagesAID();

// <>{% endif %}
// <>{% endfor %}
