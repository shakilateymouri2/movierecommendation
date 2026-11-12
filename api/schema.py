from pydantic import BaseModel, Field, field_validator

class MovieRequest(BaseModel):
    title: str = Field(..., max_length=50)
    limit: int = Field(default=5, ge=1, le=20)

    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        if not value.strip():
            raise ValueError("Title cannot be empty.")
        return value.strip()


class MovieRecommendation(BaseModel):
    id: int
    title: str = Field(..., max_length=50)