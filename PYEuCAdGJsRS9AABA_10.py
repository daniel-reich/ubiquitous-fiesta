
class CoffeeShop:
    def __init__(self, name, menu, orders):
        self.name = name
        self.menu = menu
        self.orders = orders
        self.total = 0
        self.min_item_price = 9999.99
        self.min_item_name = ''
        self.drinks = []
        self.food = []
​
    def add_order(self, item):
        self.item = item
        for x in self.menu:
            if x['item'] == self.item:
                self.orders.append(self.item)
                self.total += x['price']
                return "Order added!"
        return "This item is currently unavailable!"
        
    def fulfill_order(self):
        if len(self.orders) > 0:
            var = self.orders[0]
            del self.orders[0]
            return "The {} is ready!".format(var)
        else:
            self.total = 0
            return "All orders have been fulfilled!"
​
    def list_orders(self):
        return self.orders
​
    def due_amount(self):
        return round(self.total, 2)
​
    def cheapest_item(self):
        for x in self.menu:
            if x['price'] < self.min_item_price:
                self.min_item_price = x['price']
                self.min_item_name = x['item']
        return self.min_item_name
​
    def drinks_only(self):
        for x in self.menu:
            if x['type'] == 'drink':
                self.drinks.append(x['item'])
        return self.drinks
​
    def food_only(self):
        for x in self.menu:
            if x['type'] == 'food':
                self.food.append(x['item'])
        return self.food

