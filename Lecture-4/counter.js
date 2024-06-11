document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("button").onclick = count;
});

let counter = 0

function count() {
    counter += 1;
    document.querySelector("#counter").innerHTML = counter;
}