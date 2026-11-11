from sentence_transformers import SentenceTransformer
#generating embedding for overview
model = SentenceTransformer("all-MiniLM-L6-v2")
from preprocessing import movie_data
import numpy as np

texts = movie_data["overview"].tolist()

embeddings = model.encode(
    texts,
    batch_size=32,
    show_progress_bar=True,
    convert_to_numpy=True
)
np.save("embeddings.npy",embeddings)
print(embeddings.shape)
