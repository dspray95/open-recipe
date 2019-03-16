# -*- coding: utf-8 -*-
import scrapy

class RecipeSpider(scrapy.Spider):
    name = 'recipe'
    start_urls = []

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
        yield{
            'title': recipe_title.get(),
            'author': attrib.get(),
            'ingredients': ingredients.getall(),
            'method': method.getall()
        }
        pass
