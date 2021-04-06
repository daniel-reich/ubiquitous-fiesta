
class CoffeeShop:
    def __init__(self, name, menu, orders):
        self.name = name
        self.menu = menu
        self.orders = orders
​
    def add_order(self, order):
        for i in self.menu:
            if i['item'] == order:
                self.orders.append(order)
                return 'Order added!'
        return 'This item is currently unavailable!'
​
    def fulfill_order(self):
        if len(self.orders) > 0:
            msg = 'The ' + self.orders[0] +' is ready!'
            self.orders.pop(0)
            return msg
        else:
            return 'All orders have been fulfilled!'
​
    def list_orders(self):
        return self.orders
​
    def due_amount(self):
        total = 0
        for i in self.orders:
            for k in self.menu:
                if k['item'] == i:
                    total += k['price']
        total = round(total, 5)
        return total
​
    def cheapest_item(self):
        cheap = 100000
        cheap_name = ''
        for i in self.menu:
            if i['price'] < cheap:
                cheap = i['price']
                cheap_name = i['item']
        return cheap_name
​
    def drinks_only(self):
        drinks = []
        for i in self.menu:
            if i['type'] == 'drink':
                drinks.append(i['item'])
        return drinks
​
    def food_only(self):
        foods = []
        for i in self.menu:
            if i['type'] == 'food':
                foods.append(i['item'])
        return foods

