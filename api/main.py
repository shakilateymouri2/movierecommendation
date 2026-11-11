from fastapi import FastAPI,HTTPException
from src.content_based.final_recommendation import MovieRecommender
app = FastAPI()
recommend = MovieRecommender()

@app.get("/recommendation{movie_title}")
def get_movie(movie_title: str):
    recommendation = recommend.recommend(movie_title)
    if recommendation is None:
        raise HTTPException(status_code=404,
                            detail="not found")
    else:
        return recommendation.to_dict(orient="records")
