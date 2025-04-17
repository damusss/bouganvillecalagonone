// APARTMENT SWAP
const apartmentCont = document.getElementById("apartment-grid-2");
const firstChild = apartmentCont.children[0];
const secondChild = apartmentCont.children[1];

function swapForLargeDevices() {
    if (window.matchMedia("(min-width: 1024px)").matches) {
        apartmentCont.insertBefore(secondChild, firstChild);
    } else {
        apartmentCont.insertBefore(firstChild, secondChild);
    }
}

swapForLargeDevices();
window.addEventListener("resize", swapForLargeDevices);


