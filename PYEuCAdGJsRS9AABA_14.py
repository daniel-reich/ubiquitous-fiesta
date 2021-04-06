
class CoffeeShop:
    def __init__(self, name, menu, orders):
        self.name = name
        self.menu = menu
        self.orders = []
        self.amount = []
        
    def add_order(self, other):
        for line in self.menu:
            if line['item'] == other:
                self.orders.append(other)
                self.amount.append(line['price'])
                return "Order added!"
        return "This item is currently unavailable!"
    
    def fulfill_order(self):
        if self.orders:
            self.amount.pop(0)
            return "The {} is ready!".format(self.orders.pop(0))
        else:
            return "All orders have been fulfilled!"
        
    def list_orders(self):
        return self.orders
    
    def due_amount(self):
        return round(sum(self.amount), 2) if self.amount else 0
        
    def cheapest_item(self):
        return min(self.menu, key = lambda x: x['price'])['item']
    
    def drinks_only(self):
        
        return [line['item'] for line in self.menu if line['type'] == 'drink']
    
    def food_only(self):
        return [line['item'] for line in self.menu if line['type'] == 'food']

