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
movie_data = movie_data.merge(credits_data,left_on ="id",right_on="movie_id")
movie_data.info()
movie_data =movie_data.drop(columns=["movie_id"])
print(movie_data.isnull().sum())
print(movie_data.duplicated().sum())
print(movie_data.dtypes)
movie_data=movie_data.drop_duplicates()
movie_data=movie_data.drop(columns=["spoken_languages"])
movie_data["genre"] = movie_data["genres"].apply(lambda x: [item["name"]for item in json.loads(x)])
movie_data = movie_data.drop(columns=["genres"])
movie_data["keywords"][0]
movie_data["cast_clean"] = movie_data["cast"].apply(
    lambda x: [item["name"] for item in json.loads(x)][:5]
)
movie_data["keywords_clean"] = movie_data["keywords"].apply(
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

movie_data["director"] = movie_data["crew"].apply(get_director)
movie_data = movie_data.drop(
    columns=["keywords", "cast", "crew"]
)
print(movie_data.isnull().sum())
print(movie_data.shape)
movie_data = movie_data.dropna(subset=["overview"])
print(movie_data.isnull().sum())
for i in movie_data.columns: 
    print(movie_data[i].head(2))
print((movie_data["title_x"] == movie_data["title_y"]).all())
movie_data = movie_data.drop(columns="title_y")
movie_data.to_parquet("models/movie_data.parquet",index=False)