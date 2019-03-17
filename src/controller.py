import os
import urllib.request
from scrapy.crawler import CrawlerProcess
from recipe_builder.recipe_builder.spiders.recipe import GoodFoodSpider
from datetime import datetime


class Controller:

    @staticmethod
    def get_recipes_url_list():
        """
        Makes sure that the required directories are set up and that we have a copy
        of the recipes.csv file downloaded
        """
        directory = "../data/input"
        filename = "recipes.csv"
        if not os.path.exists(directory):
            os.mkdir(directory)
        if not os.path.isfile(directory + "/" + filename):
            recipe_csv_url = "https://docs.google.com/spreadsheets/d/" \
                             "1l3vf7RfApXYlh1b1uMpExacXw4V6jJ0y3wr2yntM8ko/export?format=csv"
            urllib.request.urlretrieve(recipe_csv_url, directory + '/' + filename)

    @staticmethod
    def run_spider(verbose=False, sample=0):
        """
        Sets up a scrapy CrawlerProcess and performs crawling for AllRecipes and BBC Good Food
        Spiders
        :param verbose: prints additional information when true
        :param sample: If greater than 0, will only crawl for n=sample urls
        """
        # Check to make sure we have the recipes csv downloaded
        Controller.get_recipes_url_list()

        # Scrapy spider setup
        spider = GoodFoodSpider(sample=sample)
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'FEED_FORMAT': "json",
            'FEED_URI': "../data/output/" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".json"
        })

        # Start crawling
        data = []
        process.crawl(spider, sample=sample)
        process.start()
        if verbose:
            print(data)

