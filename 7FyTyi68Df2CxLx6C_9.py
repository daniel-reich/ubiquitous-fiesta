
class Pizza:
    count = 0
    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.count += 1
        self.order_number = Pizza.count
​
    @classmethod
    def garden_feast(cls):
        ingredients = ["spinach", "olives", "mushroom"]
        return cls(ingredients)
    
    @classmethod
    def meat_festival(cls):
        ingredients = ["beef", "meatball", "bacon"]
        return cls(ingredients)
​
    @classmethod
    def hawaiian(cls):
        ingredients = ["ham", "pineapple"]
        return cls(ingredients)

