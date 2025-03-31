function searchRecipe() {
    let ingredient = document.getElementById("ingredientInput").value.trim();
    let cuisine = document.getElementById("cuisineInput").value.trim();
    let diet = document.getElementById("dietInput").value;

    let url = `http://127.0.0.1:5000/search?ingredient=${ingredient}&cuisine=${cuisine}&diet=${diet}`;

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error("No recipes found! Check your input.");
            }
            return response.json();
        })
        .then(data => {
            displayResults(data);
        })
        .catch(error => {
            document.getElementById("results").innerHTML = `<p style="color:red;">${error.message}</p>`;
        });
}

function displayResults(recipes) {
    let resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = "";

    recipes.forEach(recipe => {
        let card = document.createElement("div");
        card.classList.add("recipe-card");

        let title = document.createElement("h3");
        title.textContent = recipe.name;

        let steps = document.createElement("p");
        steps.innerHTML = `<strong>Steps:</strong><br>` + recipe.steps.map((step, i) => `${i + 1}. ${step}`).join("<br>");

        let speakBtn = document.createElement("button");
        speakBtn.textContent = "🔊 Read Recipe";
        speakBtn.onclick = () => readRecipe(recipe.name, recipe.steps);

        card.appendChild(title);
        card.appendChild(steps);
        card.appendChild(speakBtn);
        resultsDiv.appendChild(card);
    });
}

function readRecipe(title, steps) {
    let text = `${title}. Steps: ` + steps.join(". ");
    let speech = new SpeechSynthesisUtterance(text);
    speech.lang = "en-US";
    window.speechSynthesis.speak(speech);
}
