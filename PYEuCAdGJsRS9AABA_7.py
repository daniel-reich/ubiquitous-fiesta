
class CoffeeShop:
​
    def __init__(self, name, menu, list=[]):
        self.name = name
        self.menu = menu
        self.orders = list
​
​
​
​
    def add_order(self, other):
        listname = []
​
        d = "This item is currently unavailable!"
        for dictionary in self.menu:
            listname.append(dictionary["item"])
        if other in listname:
            d = 'Order added!'
            self.orders.append(other)
        return d
​
​
    def list_orders(self):
        return self.orders
​
​
​
    def fulfill_order(self):
        if self.orders:
            c = self.orders.pop(0)
            return "The {} is ready!".format(c)
        else:
            return "All orders have been fulfilled!"
​
​
    def due_amount(self):
        due = 0
        for dict2 in self.menu:
            if dict2['item'] in self.orders:
                due += dict2['price']
        return round(due, 2)
​
​
    def cheapest_item(self):
        pricelist = []
        for dict2 in self.menu:
            pricelist.append(dict2["price"])
        a = min(pricelist)
        for dict2 in self.menu:
            if dict2["price"] == a:
                cheap = dict2["item"]
        return cheap
​
​
    def food_only(self):
        listfood = []
        for dict0 in self.menu:
            if dict0['type'] == "food":
                listfood.append(dict0['item'])
        return listfood
​
​
    def drinks_only(self):
        drinks = []
        for dict3 in self.menu:
            if dict3["type"] == "drink":
                drinks.append(dict3['item'])
        return drinks

