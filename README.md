# XNL-21BCG10126-LLM-1
XNL-21BCG10126-LLM-1
🚀 FinTech LLM System for market sentiment analysis, fraud detection, financial report summarization, and personalized financial recommendations.

📌 Features
Multi-LLM Deployment: Supports GPT-4-Turbo, Bloom, LLaMA, Mixtral, and Falcon.
Market Sentiment Analysis: Analyzes financial news and social media trends.
Financial Report Summarization: Extracts insights from SEC/EDGAR 10-K reports.
Fraud Detection: Uses Neo4j GraphDB to detect anomalies in transactions.
Real-time Market Data Scraping: Fetches stock, crypto, and forex data from:
Binance API
Alpha Vantage
Yahoo Finance
AI Agents for Financial Decision Making:
Market Data Aggregator
Risk Assessment Agent
LLM Sentiment Analyzer
Trade Execution AI
Fraud Detection Agent
Portfolio Manager
Compliance & Regulatory Agent

## 📂 Project Structure


XNL-21BCG10126-LLM-1/
│── src/                   # Core source code
│   ├── main.py            # FastAPI entry point
│   ├── models/            # LLM handling & financial models
│   ├── agents/            # AI agents for financial tasks
│   ├── data_ingestion/    # Market data scraping modules
│   ├── fraud_detection/   # Graph-based fraud detection
│   ├── utils/             # Helper functions
│── requirements.txt       # Python dependencies
│── Dockerfile             # Docker setup
│── README.md              # Project documentation
│── .env.example           # Sample environment variables
│── config.yaml            # Configuration settings


# Quickstart
1️⃣ Clone the Repository
git clone https://github.com/Itachi0710/XNL-21BCG10126-LLM-1.git
cd XNL-21BCG10126-LLM-1

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Set Up Environment Variables
Copy the .env.example file and update credentials:
cp .env.example .env

4️⃣ Run the FastAPI Server
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

# 🐳 Running with Docker
1. Build the Image
docker build -t env .

2. Run the Container
docker run -d -p 8000:8000 env

3. Check Running Containers
docker ps


# 📜 API Endpoints
Endpoint	         Method	         Description
/predict_sentiment	 POST	    Analyzes market sentiment
/summarize_report	 POST	    Summarizes financial reports
/detect_fraud	     POST	    Identifies fraudulent activities
/get_market_data	 GET	    Fetches live market data
/trade_decision	    POST	     Suggests trade execution


# 📌 Bonus Done
 Add Reinforcement Learning for Trade Execution AI
 Improve fraud detection using GNNs
 Integrate custom embeddings for finance-specific LLM tuning