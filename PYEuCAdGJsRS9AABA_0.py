
class CoffeeShop:
​
    def __init__(self, name, menu, orders):
        self.name = name
        self.menu = menu
        self.orders = orders
​
    def add_order(self, order):
        if any(item["item"] == order for item in self.menu):
            self.orders.append(order)
            return "Order added!"
        else:
            return "This item is currently unavailable!"
​
    def list_orders(self):
        return self.orders
​
    def due_amount(self):
        return round(sum(present["price"] for item in self.orders
                         for present in self.menu
                         if present["item"] == item), 2)
​
    def fulfill_order(self):
        if self.orders:
            ready_item = self.orders[0]
            self.orders = self.orders[1:]
            return "The {} is ready!".format(ready_item)
        else:
            return "All orders have been fulfilled!"
​
    def cheapest_item(self):
        return min(self.menu, key=lambda d: d["price"])["item"]
​
    def drinks_only(self):
        return [item["item"] for item in self.menu if item["type"] == "drink"]
​
    def food_only(self):
        return [item["item"] for item in self.menu if item["type"] == "food"]

