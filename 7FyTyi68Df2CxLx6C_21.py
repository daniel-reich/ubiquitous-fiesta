
num=0
class Pizza(object):
    def __init__(self,liste):
        global num
        num=num+1
        self.ingredients=liste
        self.order_number=num
​
    def garden_feast():
        return Pizza(["spinach", "olives", "mushroom"])
    def hawaiian():
        return Pizza(["ham", "pineapple"])
    def meat_festival():
        return Pizza(["beef", "meatball", "bacon"])
Pizza.garden_feast=staticmethod(Pizza.garden_feast)

