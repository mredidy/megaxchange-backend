from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class BridgeRequest(BaseModel):
    tx_hash: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/bridge")
def bridge_tokens(request: BridgeRequest):
    # Simulate bridge logic — placeholder for Sepolia tx verification + MegaETH mint
    if not request.tx_hash.startswith("0x") or len(request.tx_hash) != 66:
        raise HTTPException(status_code=400, detail="Invalid transaction hash format")

    # Mock response (replace with actual RPC/mint call later)
    return {
        "status": "submitted",
        "message": f"Bridge initiated for Sepolia tx {request.tx_hash}"
    }