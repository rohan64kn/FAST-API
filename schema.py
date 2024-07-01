from typing import Optional
from pydantic import BaseModel


class MovieBase(BaseModel):
    movie_name: str
    director: str
    geners: str
    cast: str


class MovieAdd(MovieBase):
    movie_id: str
    streaming_platform: Optional[str] = None
    membership_required: bool
    class Config:
        orm_mode = True


class Movie(MovieAdd):
    id: int

    class Config:
        orm_mode = True


class UpdateMovie(BaseModel):

    movie_id: str
    streaming_platform: Optional[str] = None
    membership_required: bool

    class Config:
        orm_mode = True

class UpdateColumnName(BaseModel):
    movie_id: str
    movie_name : str
    director : str
    geners : str
    membership_required : bool
    cast : str
    streaming_platform: Optional[str] = None

    class config:
        orm_mode = True