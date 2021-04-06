
class Pizza:
    _order_number = 0
​
    def __init__(self, ingredients: list):
        self._ingredients = ingredients
        Pizza._order_number += 1
        self.order_number = Pizza._order_number
​
    @property
    def ingredients(self):
        return self._ingredients
​
    @ingredients.setter
    def ingredients(self, ingredients: list):
        self._ingredients = ingredients
​
    @classmethod
    def hawaiian(cls):
        ingredients = ['ham', 'pineapple']
        return cls(ingredients)
​
    @classmethod
    def meat_festival(cls):
        ingredients = ['beef', 'meatball', 'bacon']
        return cls(ingredients)
​
    @classmethod
    def garden_feast(cls):
        ingredients = ['spinach', 'olives', 'mushroom']
        return cls(ingredients)

