
const form = document.getElementById("recommendationForm");

const movieTitle = document.getElementById("movieTitle");
const limit = document.getElementById("limit");

const results = document.getElementById("results");
const message = document.getElementById("message");
const searchButton = document.getElementById("searchButton");

form.addEventListener("submit", async function(event) {

    event.preventDefault();

    const title = movieTitle.value.trim();
    const numberOfMovies = limit.value;

    if (!title) {
        message.textContent = "لطفاً نام فیلم را وارد کن.";
        return;
    }

    searchButton.disabled = true;
    searchButton.textContent = "در حال جستجو...";
    message.textContent = "";
    results.innerHTML = "";

    try {

        const url =
            `http://127.0.0.1:8000/recommendation/${encodeURIComponent(title)}?limit=${numberOfMovies}`;

        const response = await fetch(url);

        if (!response.ok) {

            if (response.status === 404) {
                throw new Error("فیلم موردنظر پیدا نشد.");
            }

            throw new Error("در دریافت اطلاعات مشکلی پیش آمد.");
        }

        const movies = await response.json();

        if (movies.length === 0) {
            message.textContent = "فیلم پیشنهادی‌ای پیدا نشد.";
            return;
        }

        message.textContent = `${movies.length} فیلم مشابه پیدا شد.`;

        movies.forEach(function(movie, index) {

            const card = document.createElement("div");
            card.classList.add("movie-card");

            const number = document.createElement("p");
            number.classList.add("movie-number");
            number.textContent = `FILM ${index + 1}`;

            const title = document.createElement("h3");
            title.textContent = movie.title;

            const id = document.createElement("p");
            id.classList.add("movie-id");
            id.textContent = `Movie ID: ${movie.id}`;

            card.append(number, title, id);
            results.appendChild(card);

        });

    } catch (error) {

        message.textContent = error.message;

    } finally {

        searchButton.disabled = false;
        searchButton.textContent = "پیدا کردن فیلم‌ها";

    }

});
