from twisted.internet import reactor
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


class BBCFoodSpider(scrapy.Spider):
    name = "bbcfood"
    allowed_domains = ["bbc.co.uk"]

    def start_requests(self):
        urls = ["http://www.bbc.co.uk/food/cuisines"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        root_path = "//li[@class='cuisine']"
        # Must precede xpath with "." to specifiy paths within quote class
        cuisine_path = "//div[@class='column']/h1/text()"

        test_path = "//div[@class='module grouped-resource-list-module']" \
                    "/h2/text()"
        next_path = ".//a/@href"
        print(response.url)
        if response.url != "http://www.bbc.co.uk/food/cuisines":
            yield {"title": response.xpath(cuisine_path).extract_first(),
                   "test": response.xpath(test_path).extract_first()}
        for cuisine in response.xpath(root_path):
            next_page = cuisine.xpath(next_path).extract_first()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(url=next_page, callback=self.parse)


def run():
    settings = get_project_settings()
    settings.set("FEED_FORMAT", "json")
    settings.set("FEED_URI", "bbcfood.json")

    configure_logging()
    runner = CrawlerRunner(settings=settings)

    d = runner.crawl(BBCFoodSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()  # script blocks here until crawler finishes


if __name__ == "__main__":
    run()
