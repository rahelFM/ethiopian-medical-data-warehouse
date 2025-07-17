# Ethiopian Medical Telegram Data Pipeline

This project is an end-to-end data platform that scrapes public Telegram channels related to Ethiopian medical businesses, stores the data in a structured raw format (data lake), and prepares it for transformation and enrichment in a modern ELT pipeline. The goal is to analyze product mentions, image content, pricing trends, and posting activity.

---

## 🚀 Project Objectives

- Scrape messages and images from public Telegram channels.
- Store raw, partitioned data in a data lake.
- Load the raw data into PostgreSQL for transformation.
- Prepare for YOLOv8 image enrichment and analytical API deployment using FastAPI.

---

## 📁 Project Structure

```bash
.
├── data/
│   └── raw/
│       └── telegram_messages/
│           └── YYYY-MM-DD/
│               └── channel_name.json
│           └── images/
│               └── channel_name/
├── scripts/
│   ├── scrape_telegram.py      # Scrapes messages and images from Telegram
│   ├── load_raw_to_postgres.py # Loads JSON data into raw.telegram_messages table
│   └── test.py                 # One-time login script for Telegram (session setup)
├── Dockerfile
├── docker-compose.yml
├── .env                        # Environment variables (not committed)
├── .gitignore
├── requirements.txt
└── README.md
✅ Tasks Completed
🔧 Task 0: Project Setup & Environment Management
✅ Initialized Git repository

✅ Created requirements.txt with all dependencies (Telethon, dbt, FastAPI, YOLO, Dagster, etc.)

✅ Wrote Dockerfile and docker-compose.yml to containerize the app and database

✅ Configured .env file for secrets (Telegram API credentials, DB settings)

✅ Verified reproducible local setup

📥 Task 1: Data Scraping and Collection
✅ Used Telethon to scrape messages and images from public channels like:

@lobelia4cosmetics

@tikvahpharma

✅ Stored raw message data in:

bash
Copy
Edit
data/raw/telegram_messages/YYYY-MM-DD/channel_name.json
✅ Downloaded image content to:

swift
Copy
Edit
data/raw/telegram_messages/images/channel_name/
✅ Saved structured JSON for each message (message ID, date, text, media type, etc.)

✅ Implemented robust session handling using anon.session via Telethon login script

🛠 Setup Instructions
Clone the repo

bash
Copy
Edit
git clone <your-repo-url>
cd ethiopian-medical-data-pipeline
Configure environment variables

docker-compose build
docker-compose run app bash
Authenticate with Telegram once

bash
Copy
Edit
python scripts/test.py
Run the scraper

bash
Copy
Edit
python scripts/scrape_telegram.py
📌 Next Steps
✅ Load raw JSON into PostgreSQL using scripts/load_raw_to_postgres.py

🔜 Set up dbt transformation pipeline (staging and marts)

🔜 Enrich data using YOLOv8 object detection

🔜 Expose data via FastAPI analytical endpoints

🔜 Orchestrate the full pipeline using Dagster

👩🏽‍💻 Contributors
Rahel Sileshi Abdisa

10 Academy Week 7 Challenge – Shipping a Data Product
