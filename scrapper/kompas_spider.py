import scrapy
from scrapy.crawler import CrawlerProcess
import json


class KompasSpider(scrapy.Spider):
    name = 'kompas'

    topics = {
        'Trending': 'https://www.kompas.com/terkini',
        'Tekno': 'https://tekno.kompas.com/index',
        'Otomotif': 'https://otomotif.kompas.com/index',
        'Bola': 'https://bola.kompas.com/index',
        'Lifestyle': 'https://lifestyle.kompas.com/index',
        'Health': 'https://health.kompas.com/index',
        'Money': 'https://money.kompas.com/index',
        'Properti': 'https://properti.kompas.com/index',
        'Edukasi': 'https://edukasi.kompas.com/index',
        'Travel': 'https://travel.kompas.com/index'
    }

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'ROBOTSTXT_OBEY': False,
        'CONCURRENT_REQUESTS': 8,
        'DOWNLOAD_DELAY': 1,
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 1,
        'AUTOTHROTTLE_MAX_DELAY': 3,
    }

    def __init__(self, *args, **kwargs):
        super(KompasSpider, self).__init__(*args, **kwargs)
        self.results = {topic: [] for topic in self.topics.keys()}
        self.article_count = {topic: 0 for topic in self.topics.keys()}
        self.max_articles_per_topic = 100

    def start_requests(self):
        for topic, url in self.topics.items():
            yield scrapy.Request(
                url=url,
                callback=self.parse_listing,
                meta={'topic': topic, 'page': 1}
            )

    def parse_listing(self, response):
        topic = response.meta['topic']

        article_links = response.css('a.article__link::attr(href)').getall()

        if not article_links:
            article_links = response.css('h3.article__title a::attr(href)').getall()
        if not article_links:
            article_links = response.css('.latest__link::attr(href)').getall()

        for link in article_links:
            if self.article_count[topic] >= self.max_articles_per_topic:
                break

            if link.startswith('http'):
                full_url = link
            else:
                full_url = response.urljoin(link)

            yield scrapy.Request(
                url=full_url,
                callback=self.parse_article,
                meta={'topic': topic}
            )
            self.article_count[topic] += 1

        if self.article_count[topic] < self.max_articles_per_topic:
            page = response.meta.get('page', 1) + 1
            next_page = f"{self.topics[topic]}?page={page}"

            if page <= 10:
                yield scrapy.Request(
                    url=next_page,
                    callback=self.parse_listing,
                    meta={'topic': topic, 'page': page}
                )

    def parse_article(self, response):
        topic = response.meta['topic']

        title = response.css('h1.read__title::text').get()
        if not title:
            title = response.css('h1::text').get()

        timestamp = response.css('.read__time::text').get()
        if not timestamp:
            timestamp = response.css('time::text').get()
        if not timestamp:
            timestamp = response.css('.article__date::text').get()

        content_paragraphs = response.css('.read__content p::text').getall()
        if not content_paragraphs:
            content_paragraphs = response.css('article p::text').getall()
        if not content_paragraphs:
            content_paragraphs = response.css('.detail__body p::text').getall()

        content = ' '.join([p.strip() for p in content_paragraphs if p.strip()])

        if title and content:
            article_data = {
                'title': title.strip(),
                'timestamp': timestamp.strip() if timestamp else '',
                'content': content[:500] if content else ''
            }
            self.results[topic].append(article_data)

    def closed(self, reason):
        output = []
        for topic, documents in self.results.items():
            if documents:
                output.append({
                    'topic': topic,
                    'documents': documents
                })

        with open('documents.json', 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=2)

        print(f"\n{'='*60}")
        print(f"Scraping completed!")
        print(f"Total articles scraped: {sum(len(docs) for docs in self.results.values())}")
        for topic, docs in self.results.items():
            print(f"  - {topic}: {len(docs)} articles")
        print(f"Results saved to documents.json")
        print(f"{'='*60}\n")


def run_spider():
    process = CrawlerProcess()
    process.crawl(KompasSpider)
    process.start()


if __name__ == '__main__':
    run_spider()
