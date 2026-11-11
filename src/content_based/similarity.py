
import numpy as np

from sklearn.metrics.pairwise import (
    pairwise_distances,
    cosine_similarity
)

from sklearn.preprocessing import MultiLabelBinarizer

from preprocessing import movie_data


# Load saved embeddings
embeddings = np.load("embeddings.npy")


# Calculate cosine similarity
overview_similarity = cosine_similarity(embeddings)


# Calculate Jaccard similarity
def calculate_jaccard(data):

    mlb = MultiLabelBinarizer()

    encoded_data = mlb.fit_transform(data)

    distance_matrix = pairwise_distances(
        encoded_data,
        metric="jaccard"
    )

    return 1 - distance_matrix


# Calculate individual similarity matrices
genre_similarity = calculate_jaccard(movie_data["genre"])

keyword_similarity = calculate_jaccard(
    movie_data["keywords_clean"]
)

cast_similarity = calculate_jaccard(
    movie_data["cast_clean"]
)

director_similarity = calculate_jaccard(
    movie_data["director"]
)


# Combine similarity matrices
final_similarity = (
    0.6 * overview_similarity +
    0.2 * genre_similarity +
    0.1 * keyword_similarity +
    0.05 * cast_similarity +
    0.05 * director_similarity
)


# Save final similarity matrix
np.save("movie_similarity.npy", final_similarity)

