from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS from anywhere (for dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to your frontend URL in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/status")
def status():
    return {
        "network": "Ethereum Sepolia",
        "status": "mock mode",
        "updated_at": "2025-04-24 14:00 UTC"
    }