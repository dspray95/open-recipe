class Nutrition:

    def __init__(self, kcal, fat, saturates, carbs, sugar, fibre, protein, salt):
        self.kcal = kcal
        self.fat = fat
        self.saturates = saturates
        self.carbs = carbs
        self.sugars = sugar
        self.fibre = fibre
        self.protein = protein
        self.salt = salt

    def to_dict(self):
        return {
            "kcal": self.kcal,
            "fat": self.fat,
            "saturates": self.saturates,
            "carbs": self.carbs,
            "sugars": self.sugars,
            "fibre": self.fibre,
            "protein": self.protein,
            "salt": self.salt
        }


class Recipe:

    def __init__(self, name, author, description, nutrition, ingredients, method, time, difficulty, servings, img_url):
        self.name = name
        self.author = author
        self.description = description
        self.nutrition = nutrition
        self.ingredients = ingredients
        self.method = method
        self.time = time,
        self.difficulty = difficulty,
        self.servings = servings
        self.img_url = img_url

    def to_dict(self):
        return {
            "name": self.name,
            "author": self.author,
            "description": self.description,
            "nutrition": self.nutrition.to_dict(),
            "ingredients": self.ingredients,
            "method": self.method,
            "time": self.time,
            "difficulty": self.difficulty,
            "servings": self.servings,
            "img_url": self.img_url
        }
