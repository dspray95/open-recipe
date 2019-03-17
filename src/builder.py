from scrapy.crawler import CrawlerProcess
from src.recipe_builder.recipe_builder.spiders.recipe import RecipeSpider
from datetime import datetime

urls = [
    'https://www.bbcgoodfood.com/recipes/775660/bigbatch-bolognese/',
    'https://www.bbcgoodfood.com/recipes/3193/buttered-sprouts-with-pancetta'
]
spider = RecipeSpider()

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': "json",
    'FEED_URI': "../data/output-" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".json"
})

data = []
process.crawl(spider)
process.start()
print(data)

def get_urls_from_data(data_path):
    print()