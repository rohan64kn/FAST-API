from fastapi import FastAPI
from appli import app
app = FastAPI(
    title="Movie Details",
    description="You can perform CRUD operation by using this API",
    version="1.0.0"
)