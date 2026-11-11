
import numpy as np
import pandas as pd

class MovieRecommender:

    def __init__(self):
        self.movie_data = pd.read_parquet(
            "models/movie_data.parquet"
        )

        self.final_similarity = np.load(
            "models/movie_similarity.npy"
        )

    def recommend(self, movie_title):
        movie_title = movie_title.strip().lower()

        movie_indices = np.flatnonzero(
            self.movie_data["title_x"].str.lower().eq(movie_title).to_numpy()
        )

        if len(movie_indices) == 0:
            return None

        movie_index = movie_indices[0]

        scores = self.final_similarity[movie_index].copy()

        scores[movie_index] = -1

        best_movies = np.argsort(scores)[-5:][::-1]

        recommendations = self.movie_data.iloc[best_movies][
            ["id", "title_x"]
        ]

        return recommendations
