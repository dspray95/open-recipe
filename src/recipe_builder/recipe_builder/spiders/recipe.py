# -*- coding: utf-8 -*-
import scrapy
from src.recipe import Recipe, Nutrition

class RecipeSpider(scrapy.Spider):
    name = 'recipe'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [
            'https://www.bbcgoodfood.com/recipes/775660/bigbatch-bolognese/',
            'https://www.bbcgoodfood.com/recipes/3193/buttered-sprouts-with-pancetta'
        ]

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
