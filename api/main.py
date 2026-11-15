from fastapi import FastAPI,HTTPException,Path,Query
from src.content_based.final_recommendation import MovieRecommender
from api.schema import  MovieRequest,MovieRecommendation
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
recommend = MovieRecommender()
@app.get("/recommendation/{movie_title}",response_model=list[MovieRecommendation])
def send_movie(    movie_title: str = Path(..., min_length=1, max_length=50),
    limit: int = Query(5, ge=1, le=20)):
     recommendation = recommend.recommend(movie_title,limit)
     if recommendation is None or recommendation.empty:
            raise HTTPException(status_code=404,
                                detail="not found")
     else:
            return recommendation.to_dict(orient="records")
    