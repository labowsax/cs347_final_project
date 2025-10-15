
document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("searchBox");
    const button = document.getElementById("submit-search");
    const searchList = document.getElementById("search-list");
    const apiSearchPrefix = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=ZYIHMGpSmgzwCecsbSxa7rSNizrdeitAiug86jlZ&query=';
    let foodResponse = null;
    let foodCard = null;
    const numberOfListItems = 4;

    function echoTokens() {
        totalHits = 0;
        const query = input.value.trim();
        if (!query) return;
        const encoded = encodeURIComponent(query);
        const finalQuery = apiSearchPrefix + encoded;
        fetch(finalQuery)
            .then(response => response.json())
            .then(data => {
                for (i = 0; i < 4; i++) {
                    foodResponse = data.foods[i];
                    console.log("✅ API Response:", data.foods[i]);
                    foodCard = document.createElement('li');
                    foodCard.innerText = foodResponse.description;
                    searchList.appendChild(foodCard);
                }
                console.log(totalHits);
            })
    }

    // Run when clicking the search span
    button.addEventListener("click", echoTokens);

    // Also run when pressing Enter
    input.addEventListener("keyup", e => {
        if (e.key === "Enter") echoTokens();
    });
});