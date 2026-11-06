import numpy as np
import pandas as pd
import json
from sentence_transformers import SentenceTransformer

movie_data = pd.read_csv("data/tmdb_5000_movies (1).csv")
credits_data = pd.read_csv("data/tmdb_5000_credits.csv")
movie_data.info()
credits_data.info()
(credits_data.iloc[0])
#eliminate extra columns 
movie_data=movie_data.drop(columns=["budget","homepage","popularity","production_countries",
"production_companies","release_date","revenue",
"runtime","status","tagline"])
project_data = movie_data.merge(credits_data,left_on ="id",right_on="movie_id")
project_data.info()
project_data =project_data.drop(columns=["movie_id"])
print(project_data.isnull().sum())
print(project_data.duplicated().sum())
print(project_data.dtypes)
project_data=project_data.drop_duplicates()
project_data=project_data.drop(columns=["spoken_languages"])
project_data["genre"] = project_data["genres"].apply(lambda x: [item["name"]for item in json.loads(x)])
project_data = project_data.drop(columns=["genres"])
project_data["keywords"][0]
project_data["cast_clean"] = project_data["cast"].apply(
    lambda x: [item["name"] for item in json.loads(x)][:5]
)
project_data["keywords_clean"] = project_data["keywords"].apply(
    lambda x: [item["name"] for item in json.loads(x)]
)
def get_director(crew):
    crew = json.loads(crew)

    directors = [
        item["name"]
        for item in crew
        if item["job"] == "Director"
    ]

    return directors

project_data["director"] = project_data["crew"].apply(get_director)
project_data = project_data.drop(
    columns=["keywords", "cast", "crew"]
)
print(project_data.isnull().sum())
print(project_data.shape)
project_data = project_data.dropna(subset=["overview"])
print(project_data.isnull().sum())
for i in project_data.columns: 
    print(project_data[i].head(2))
print((project_data["title_x"] == project_data["title_y"]).all())
project_data = project_data.drop(columns="title_y")

#generating embedding for overview
model = SentenceTransformer("all-MiniLM-L6-v2")

texts = project_data["overview"].tolist()

embeddings = model.encode(
    texts,
    batch_size=32,
    show_progress_bar=True,
    convert_to_numpy=True
)
np.save("embeddings.npy",embeddings)
print(embeddings.shape)