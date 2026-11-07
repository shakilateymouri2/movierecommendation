from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load movie embeddings
embeddings = np.load("embeddings.npy")

# Calculate cosine similarity between all movies
similarity_matrix = cosine_similarity(embeddings)

# Check results
print("Similarity matrix shape:", similarity_matrix.shape)
print("Data type:", similarity_matrix.dtype)

# Save similarity matrix
np.save("movie_similarity.npy", similarity_matrix)