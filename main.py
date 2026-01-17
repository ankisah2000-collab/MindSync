from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import users, feed

app = FastAPI(title="Mental Health & Wellness Recommendation System")

# CORS setup for frontend communication
origins = [
    "http://localhost:5173", # Vite default port
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(feed.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Mental Health Recommendation Engine API"}
