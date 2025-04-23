# MegaXchange Backend

## Overview

The MegaXchange backend provides the core bridging logic for transferring ETH from the Sepolia testnet to the MegaETH testnet. This service verifies Sepolia transactions and initiates the minting of corresponding ETH on the MegaETH network. It is designed to be modular, scalable, and suitable for integration with frontend clients or other APIs.

## Features

- **Transaction Validation**: Checks Sepolia transactions for authenticity and correctness.
- **Minting Execution**: Sends mint requests to the MegaETH testnet upon successful validation.
- **API Endpoints**: RESTful endpoints for bridge operations.
- **Logging & Monitoring**: Provides clear logs for transaction flow and error tracking.

## Technologies Used

- **FastAPI**: Modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **Render**: Cloud platform used for deploying the backend service.
- **Ethers.js / Web3.py**: Blockchain SDKs for interacting with Ethereum-based networks.
- **Sepolia RPC / MegaETH RPC**: Used to communicate with both testnets.

## Setup and Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/mredidy/megaxchange-backend.git
    ```

2. **Navigate to the Project Directory**

    ```bash
    cd megaxchange-backend
    ```

3. **Install Dependencies**

    It's recommended to use a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

4. **Set Environment Variables**

    Create a `.env` file and include necessary environment variables such as:

    ```env
    SEPOLIA_RPC_URL=<your_sepolia_rpc_url>
    MEGAETH_RPC_URL=<your_megaeth_rpc_url>
    PRIVATE_KEY=<wallet_private_key>
    ```

5. **Run the Application**

    ```bash
    uvicorn main:app --reload
    ```

    The API will be accessible at `http://localhost:8000`.

6. **Deploy to Render**

    - Connect the repository to [Render](https://render.com).
    - Add environment variables in the Render dashboard.
    - Deploy as a web service.

## API Endpoints

| Method | Endpoint         | Description                                 |
|--------|------------------|---------------------------------------------|
| POST   | `/bridge`        | Submits a Sepolia tx hash to trigger minting |
| GET    | `/status/{tx}`   | Returns the status of a bridging operation   |
| GET    | `/health`        | Health check for uptime monitoring          |

## Project Structure

- `main.py`: FastAPI entry point.
- `services/`: Logic for transaction validation, minting, and RPC communication.
- `schemas/`: Request and response models.
- `utils/`: Utility functions for signing, logging, etc.

## Contributing

Contributions are welcome. Please fork the repository and open a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For support or inquiries, contact:  
**Email**: misteredidy@gmail.com