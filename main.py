from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://megaxchange-frontend.vercel.app"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BridgeRequest(BaseModel):
    tx_hash: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/bridge")
def bridge_tokens(request: BridgeRequest):
    if not request.tx_hash.startswith("0x") or len(request.tx_hash) != 66:
        raise HTTPException(status_code=400, detail="Invalid transaction hash format")

    return {
        "status": "submitted",
        "message": f"Bridge initiated for Sepolia tx {request.tx_hash}"
    }