# Kompas.com News Scraper

A Scrapy-based web scraper for collecting news articles from Kompas.com across multiple topics.

## Topics Covered

- Trending
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

The scraper generates `documents.json` with the following structure:

```json
[
  {
    "topic": "Tekno",
    "documents": [
      {
        "title": "Article title",
        "timestamp": "27 Desember 2025, 16:38 WIB",
        "content": "Article content..."
      }
    ]
  }
]
```

## How to Run

From the project root directory:

```bash
uv run python scrapper/kompas_spider.py
```

The scraper will:
- Fetch up to 100 articles per topic (1000 total)
- Save results to `documents.json` in the project root
- Display progress and summary upon completion

## Configuration

Edit `kompas_spider.py` to adjust:
- `max_articles_per_topic`: Number of articles per topic (default: 100)
- `DOWNLOAD_DELAY`: Delay between requests (default: 1 second)
- `CONCURRENT_REQUESTS`: Number of parallel requests (default: 8)
