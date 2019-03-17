import csv
from scrapy.crawler import CrawlerProcess
from recipe_builder.recipe_builder.spiders.recipe import RecipeSpider
from datetime import datetime


def run_spider():
    spider = RecipeSpider()

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': "json",
        'FEED_URI': "../data/output/" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".json"
    })

    data = []
    process.crawl(spider)
    process.start()
    print(data)


run_spider()