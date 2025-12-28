import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime


TOPICS = {
    'Trending': 'https://www.kompas.com/terkini',
    'Tekno': 'https://tekno.kompas.com',
    'Otomotif': 'https://otomotif.kompas.com',
    'Bola': 'https://bola.kompas.com',
    'Lifestyle': 'https://lifestyle.kompas.com',
    'Health': 'https://health.kompas.com',
    'Money': 'https://money.kompas.com',
    'Properti': 'https://properti.kompas.com',
    'Edukasi': 'https://edukasi.kompas.com',
    'Travel': 'https://travel.kompas.com'
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
}


def fetch_article_links(url, max_links=10):
    """Fetch article links from a topic page"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        links = []

        for a in soup.find_all('a', href=True):
            href = a['href']
            if '/read/' in href:
                if href.startswith('http'):
                    links.append(href)
                else:
                    links.append(requests.compat.urljoin(url, href))

                if len(links) >= max_links:
                    break

        return list(set(links))[:max_links]

    except Exception as e:
        print(f"  ❌ Error fetching {url}: {e}")
        return []


def fetch_article_content(url):
    """Fetch article title, timestamp, and content"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find('h1')
        title = title.get_text(strip=True) if title else ''

        timestamp = ''
        time_elem = soup.find('div', class_='read__time')
        if time_elem:
            timestamp = time_elem.get_text(strip=True)
        else:
            time_elem = soup.find('time')
            if time_elem:
                timestamp = time_elem.get('datetime', '') or time_elem.get_text(strip=True)

        content_parts = []
        content_div = soup.find('div', class_='read__content')
        if content_div:
            paragraphs = content_div.find_all('p')
            for p in paragraphs:
                text = p.get_text(strip=True)
                if text and len(text) > 20:
                    content_parts.append(text)

        content = ' '.join(content_parts)

        return {
            'title': title,
            'timestamp': timestamp,
            'content': content
        }

    except Exception as e:
        print(f"    ⚠️  Error parsing article: {e}")
        return None


def crawl_kompas():
    """Main crawler function"""
    print("\n" + "="*70)
    print("🚀 KOMPAS.COM NEWS CRAWLER")
    print("="*70)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Target: Top 10 articles per topic (100 total)")
    print("="*70 + "\n")

    results = []
    total_articles = 0

    for topic_name, topic_url in TOPICS.items():
        print(f"\n📰 [{topic_name.upper()}]")
        print(f"   URL: {topic_url}")

        article_links = fetch_article_links(topic_url, max_links=10)
        print(f"   Found {len(article_links)} article links")

        documents = []

        for i, link in enumerate(article_links, 1):
            print(f"   [{i}/{len(article_links)}] Fetching: {link[:60]}...", end=' ')

            article_data = fetch_article_content(link)

            if article_data and article_data['title']:
                documents.append(article_data)
                total_articles += 1
                print("✓")
            else:
                print("✗")

            time.sleep(0.5)

        if documents:
            results.append({
                'topic': topic_name,
                'documents': documents
            })

        print(f"   ✅ Collected {len(documents)} articles from {topic_name}")
        time.sleep(1)

    with open('documents.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("\n" + "="*70)
    print("✨ CRAWLING COMPLETED!")
    print("="*70)
    print(f"Total articles collected: {total_articles}")
    print("\nBreakdown by topic:")
    for item in results:
        print(f"  • {item['topic']}: {len(item['documents'])} articles")
    print(f"\n💾 Results saved to: documents.json")
    print("="*70 + "\n")


if __name__ == '__main__':
    crawl_kompas()
