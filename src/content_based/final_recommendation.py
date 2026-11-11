import numpy as np
import pandas as pd
movie_data = pd.read_parquet("models/movie_data.parquet")
final_similarity = np.load("models/movie_similarity.npy")
movie_title = input("Type the movie name: ").strip().lower()

movie_indices = np.flatnonzero(
    movie_data["title_x"].str.lower().eq(movie_title).to_numpy()
)

if len(movie_indices) == 0:

    print("Movie not found!")

else:

    movie_index = movie_indices[0]

    # Get similarity scores
    scores = final_similarity[movie_index].copy()

    # Exclude the movie itself
    scores[movie_index] = -1

    # Get top 5 similar movies
    best_movies = np.argsort(scores)[-5:][::-1]

    # Display recommendations
    recommendations = movie_data.iloc[best_movies][
        ["id", "title_x"]
    ]

    print(recommendations)