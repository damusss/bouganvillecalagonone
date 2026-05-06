const clampedDescription = document.getElementById("clamped-description");
const readMoreBtn = document.getElementById("descr-read-more");
const readMoreText = document.getElementById("read-more");
const readLessText = document.getElementById("read-less");

function toggleDescriptionClamp() {
    if (clampedDescription.classList.contains("expanded-text")) {
        clampedDescription.classList.remove("expanded-text");
        clampedDescription.classList.add("clamped-text");
        readMoreBtn.innerHTML = `...${readMoreText.innerHTML}`;
    } else {
        clampedDescription.classList.remove("clamped-text");
        clampedDescription.classList.add("expanded-text");
        readMoreBtn.innerHTML = `...${readLessText.innerHTML}`;
    }
}

clampedDescription.addEventListener("click", toggleDescriptionClamp);
readMoreBtn.addEventListener("click", toggleDescriptionClamp);

const carousel = document.getElementById("carousel-images");
function scrollCarousel(direction) {
    const imageWidth = carousel.querySelector("div").offsetWidth;
    carousel.scrollBy({ left: direction * imageWidth, behavior: "smooth" });
}

let mouseDown = false;
let startX, scrollLeft;

const startDragging = (e) => {
    mouseDown = true;
    startX = e.pageX - carousel.offsetLeft;
    scrollLeft = carousel.scrollLeft;
}

const stopDragging = (e) => {
    mouseDown = false;
}

const move = (e) => {
    e.preventDefault();
    if(!mouseDown) { return; }
    const x = e.pageX - carousel.offsetLeft;
    const scroll = x - startX;
    carousel.scrollLeft = scrollLeft - scroll;
}

carousel.addEventListener('mousemove', move, false);
carousel.addEventListener('mousedown', startDragging, false);
carousel.addEventListener('mouseup', stopDragging, false);
carousel.addEventListener('mouseleave', stopDragging, false);