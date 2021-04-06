
global order_num
order_num = 1
​
class Pizza:
    def __init__(self,lst):
        global order_num
        self.order_number = order_num
        order_num += 1
        self.ingredients = lst
​
    @classmethod
    def garden_feast(self):
        return self(['spinach', 'olives', 'mushroom'])
    @classmethod
    def hawaiian(self):
        return self(['ham', 'pineapple'])
    @classmethod
    def meat_festival(self):
        return self(['beef', 'meatball', 'bacon'])

