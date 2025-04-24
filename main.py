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
def get_real_status():
    # Example: return dummy WETH transaction details from Sepolia
    return {
        "network": "Ethereum Sepolia",
        "status": "Live",
        "updated_at": "2025-04-24 16:32 UTC",
        "tx_count": 42,  # Optional: Add fields for extra insights
        "latest_tx": "0xabc123..."  # Optional
    }