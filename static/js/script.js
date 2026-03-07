document.addEventListener("DOMContentLoaded", function () {

    const track = document.querySelector(".slide-track");
    const next = document.querySelector(".next");
    const prev = document.querySelector(".prev");

    if (!track) {
        console.log("Slider not found");
        return;
    }

    let currentIndex = 0;
    const visibleCards = 3;

    function updateSlider() {
        const cards = document.querySelectorAll(".slide-card");
        const totalCards = cards.length;

        if (totalCards <= visibleCards) return;

        const cardWidth = cards[0].offsetWidth + 30;
        track.style.transform = `translateX(-${currentIndex * cardWidth}px)`;
    }

    next.addEventListener("click", function () {
        const cards = document.querySelectorAll(".slide-card");
        const totalCards = cards.length;

        currentIndex++;

        if (currentIndex > totalCards - visibleCards) {
            currentIndex = 0;
        }

        updateSlider();
    });

    prev.addEventListener("click", function () {
        const cards = document.querySelectorAll(".slide-card");
        const totalCards = cards.length;

        currentIndex--;

        if (currentIndex < 0) {
            currentIndex = totalCards - visibleCards;
        }

        updateSlider();
    });

});
// SEARCH SUGGESTION CODE (paste here)

const input = document.getElementById("searchInput");
const suggestionsBox = document.getElementById("suggestions");

input.addEventListener("keyup", function(){

    let query = input.value;

    if(query.length < 2){
        suggestionsBox.innerHTML = "";
        return;
    }

    fetch(`/suggest?q=${query}`)
    .then(response => response.json())
    .then(data => {

        suggestionsBox.innerHTML = "";

        data.suggestions.forEach(item => {

            let div = document.createElement("div");

            div.classList.add("suggestion-item");

            div.innerText = item;

            div.onclick = function(){
                input.value = item;
                suggestionsBox.innerHTML = "";
            };

            suggestionsBox.appendChild(div);

        });

    });

});