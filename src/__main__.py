import scrapy
from scrapy.crawler import CrawlerProcess
from src.recipe_builder.recipe_builder.spiders.recipe import RecipeSpider

urls = [
    'https://www.bbcgoodfood.com/recipes/775660/bigbatch-bolognese/',
    'https://www.bbcgoodfood.com/recipes/3193/buttered-sprouts-with-pancetta'
]
spider = RecipeSpider()
spider.start_urls = urls

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_URI': 'file:///tmp/export.json'
})

data = []
process.crawl(spider)
process.start()
print(data)
