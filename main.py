    # main.py
    from fastapi import FastAPI, Request
    from fastapi.middleware.cors import CORSMiddleware

    app = FastAPI()

    # Allow frontend to access the backend
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Replace with your frontend domain in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.post("/bridge")
    async def mock_bridge(request: Request):
        data = await request.json()
        print("Received mock request:", data)

        # Simulate a response
        return {
            "status": "success",
            "tx_hash": data.get("tx_hash", "0xmocktxhash"),
            "bridge_status": "pending",
            "from_chain": data.get("from_chain", "Sepolia"),
            "to_chain": data.get("to_chain", "MegaETH")
        }