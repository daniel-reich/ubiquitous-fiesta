
class CoffeeShop:
​
    def __init__(self, name, menu, orders):
        self.name = name
        self.menu = menu
        self.orders = orders
        self.amount = 0
        for item in menu:
            if item['item'] in orders:
                self.amount += item['price']
        
    def add_order(self, order):
        for item in self.menu:
            if item['item'] == order:
                self.orders.append(order)
                self.amount += item['price']
                return "Order added!"
        return "This item is currently unavailable!"
​
    def fulfill_order(self):
        if len(self.orders) == 0:
            return "All orders have been fulfilled!"
        name = self.orders.pop(0)
        for item in self.menu:
            if item['item'] == name:
                self.amount -= item['price']
        return "The " + name + " is ready!"
​
    def list_orders(self):
        return self.orders
​
    def due_amount(self):
        return abs(round(self.amount, 2))
​
    def cheapest_item(self):
        min_price = 2**13
        for item in self.menu:
            if item['price'] < min_price:
                min_price = item['price']
                cheapest = item['item']
        return cheapest
​
    def drinks_only(self):
        return [item['item'] for item in self.menu if item['type'] == "drink"]
        
    def food_only(self):
        return [item['item'] for item in self.menu if item['type'] == "food"]

