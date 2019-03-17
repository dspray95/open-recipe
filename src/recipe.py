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

    def __init__(self, name, author, nutrition, ingredients, method):
        self.name = name
        self.author = author
        self.nutrition = nutrition
        self.ingredients = ingredients
        self.method = method

    def to_dict(self):
        return {
            "name": self.name,
            "author": self.author,
            "nutrition": self.nutrition.to_dict(),
            "ingredients": self.ingredients,
            "method": self.method
        }
