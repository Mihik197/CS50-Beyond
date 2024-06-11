const questions = [
    {
        question: "What is 10 plus 10?",
        options: ["8", "27", "20", "30"],
        answer: "20"
    },
    {
        question: "What is the largest animal?",
        options: ["Lion", "Blue Whale", "Elephant", "Giraffe"],
        answer: "Blue Whale"
    },
    {
        question: "What is the fastest bird?",
        options: ["Hummingbird", "Pigeon", "Eagle", "Crow"],
        answer: "Hummingbird"
    }
];

let question_number = 0;
let correct = 0;

document.addEventListener("DOMContentLoaded", () => {
    load_question();
});

function load_question() {
    if (question_number >= 3) {
        document.querySelector("#options").remove();
        document.querySelector("#score").remove();

        document.querySelector("#question").innerHTML = `Quiz Complete! <br> You scored ${correct} out of ${question_number}!`;
    }

    document.querySelector("#question").innerHTML = questions[question_number].question;

    const options = document.querySelector("#options");
    options.innerHTML = "";
    // insert options
    questions[question_number].options.forEach((option) => {
        options.innerHTML += `<button class="option">${option}</button>`;
    });

    document.querySelectorAll(".option").forEach(option => {
        option.onclick = () => {
            if (option.textContent == questions[question_number].answer) {
                correct += 1;
            };
            
            document.querySelector("#correct").innerHTML = `${correct} of ${question_number += 1}`;

            load_question();
        };
    });
}

