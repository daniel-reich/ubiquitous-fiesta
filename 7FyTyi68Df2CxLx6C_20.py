
class Pizza:
    num = 0
    def __init__(self,ingredients):
        Pizza.num = Pizza.num+1
        self.order_number = Pizza.num
        self.ingredients = ingredients
    @staticmethod
    def hawaiian():
        return Pizza(['ham','pineapple'])
    @staticmethod
    def meat_festival():
        return Pizza(['beef', 'meatball', 'bacon'])
    @staticmethod
    def garden_feast():
        return Pizza(['spinach', 'olives', 'mushroom'])

