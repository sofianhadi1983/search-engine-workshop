# Kompas.com News Crawler

A simple web crawler for collecting news articles from Kompas.com across multiple topics.

## Topics Covered

- Tekno
- Otomotif
- Bola
- Lifestyle
- Health
- Money
- Properti
- Edukasi
- Travel

## Output Format

The crawler generates `documents.json` with the following structure:

```json
[
  {
    "topic": "Tekno",
    "documents": [
      {
        "title": "Article title",
        "timestamp": "28 Desember 2025, 11:02 WIB",
        "content": "Full article content..."
      }
    ]
  }
]
```

## How to Run

From the project root directory:

```bash
uv run python scrapper/direct_crawler.py
```

The crawler will:
- Fetch 10 articles per topic (approximately 70-100 total)
- Display real-time progress for each topic
- Save results to `documents.json` in the project root

## Features

- Real-time progress display with status indicators
- Full article content extraction
- Automatic retry on errors
- Clean JSON output format
- No external crawler framework needed

## Configuration

Edit `direct_crawler.py` to adjust:
- `max_links` parameter in `fetch_article_links()`: Number of articles per topic (default: 10)
- `HEADERS`: User agent and request headers
- `time.sleep()` delays: Request throttling (default: 0.5s between articles)
