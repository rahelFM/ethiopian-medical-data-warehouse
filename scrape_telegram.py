# scripts/scrape_telegram.py

import os
import json
import asyncio
from datetime import datetime
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv()

api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")

CHANNELS = [
    "https://t.me/lobelia4cosmetics",
    "https://t.me/tikvahpharma",
    # add more channels here if needed
]

RAW_DIR = "D:\\KAIM5\\Week7\\data\\raw\\telegram_messages"

async def scrape_channel(channel_url, limit=100):
    async with TelegramClient("anon", api_id, api_hash) as client:
        entity = await client.get_entity(channel_url)
        messages = []
        async for message in client.iter_messages(entity, limit=limit):
            data = {
                "id": message.id,
                "date": message.date.isoformat(),
                "text": message.message,
                "sender_id": getattr(message.sender_id, 'user_id', None),
                "has_media": message.media is not None,
                "media_type": type(message.media).__name__ if message.media else None
            }

            # Download images
            if isinstance(message.media, MessageMediaPhoto):
                media_dir = f"{RAW_DIR}/images/{entity.username}"
                os.makedirs(media_dir, exist_ok=True)
                img_path = await message.download_media(file=media_dir)
                data["media_path"] = img_path

            messages.append(data)

        # Save as JSON
        dt_str = datetime.now().strftime("%Y-%m-%d")
        os.makedirs(f"{RAW_DIR}/{dt_str}", exist_ok=True)
        out_path = f"{RAW_DIR}/{dt_str}/{entity.username}.json"

        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)

        print(f"[✔] Saved {len(messages)} messages from {channel_url} to {out_path}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    for ch in CHANNELS:
        loop.run_until_complete(scrape_channel(ch))
