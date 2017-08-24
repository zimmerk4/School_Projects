from twisted.internet import reactor
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


class QuoteSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = ["http://quotes.toscrape.com/page/1/"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        quote_path = "//div[@class='quote']"
        # Must precede xpath with "." to specifiy paths within quote class
        text_path = ".//span[@class='text']/text()"
        author_path = ".//small[@class='author']/text()"
        tags_path = ".//a[@class='tag']/text()"
        next_path = "//li[@class='next']/a[starts-with(@href, '/page/')]/@href"
        for quote in response.xpath(quote_path):
            yield {
                "text": quote.xpath(text_path).extract_first(),
                "author": quote.xpath(author_path).extract_first(),
                "tags": quote.xpath(tags_path).extract()
            }
        next_page = response.xpath(next_path).extract_first()
        print(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)


def run():

    settings = get_project_settings()
    settings.set("FEED_FORMAT", "json")
    settings.set("FEED_URI", "result.json")

    configure_logging()
    runner = CrawlerRunner(settings=settings)

    d = runner.crawl(QuoteSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()  # script blocks here until crawler finishes


if __name__ == "__main__":
    run()