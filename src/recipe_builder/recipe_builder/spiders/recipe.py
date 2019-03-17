# -*- coding: utf-8 -*-
import scrapy
import csv
from src.recipe import Recipe, Nutrition


class RecipeSpider(scrapy.Spider):
    name = 'recipe'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = self.get_urls_from_data("../data/input/recipes.csv")['bbc']

    @staticmethod
    def get_urls_from_data(data_path: str):
        """
        Finds and returns a list of URLs from the recipes.csv dataset.
        :param data_path:
        :return:
        """
        bbc_urls = []
        all_recipes_urls = []
        with open(data_path) as csv_file:
            csv_reader = csv.reader(csv_file)
            for index, row in enumerate(csv_reader):
                if bbc_urls.__len__() < 10:
                    if "www.bbcgoodfood.com" in row[0]:
                        bbc_urls.append(row[0])

        return {
            "bbc": bbc_urls,
            "all_recipes": all_recipes_urls
        }

    def parse(self, response):
        # Information from header includes title, author, cook time, difficulty, servings
        # and nutritional information
        header = response.xpath('//div[contains(@class, "recipe-header")]')
        recipe_title = header.xpath('h1[contains(@class, "recipe-header__title")]/text()')
        attrib = header.xpath('//div[contains(@class, "recipe-header__chef")]/span/a/text()')

        # Information from the details section includes ingredients and method
        details = response.xpath('//div[contains(@class, "responsive-tabs")]')

        # The full text of the ingredients will be in the content attribute of the li tag
        ingredients = details.xpath('section[contains(@id, "recipe-ingredients")]//'
                                    'div[contains(@class, "ingredients-list__content")]/ul/li/@content')

        # TODO Check for final method step, sometimes the beeb offers a suggestion with a link to another recipe
        method = details.xpath('section[contains(@id, "recipe-method")]//'
                               'div[contains(@class, "method")]/ol/li/p/text()')

        nutrition_object = Nutrition("kcal", "fat", "saturates", "carbs", "sugar", "fibre", "protein", "salt")
        recipe_object = Recipe(recipe_title.get(), attrib.get(), nutrition_object, ingredients.getall(), method.getall())
        # self, name, author, nutrition, ingredients, method
        return recipe_object.to_dict()
        pass
