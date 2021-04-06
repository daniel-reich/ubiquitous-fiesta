
class Smoothie:
​
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.prices = {
            "Strawberries" : "$1.50",
            "Banana" : "$0.50",
            "Mango" : "$2.50",
            "Blueberries" : "$1.00",
            "Raspberries" : "$1.00",
            "Apple" : "$1.75",
            "Pineapple" : "$3.50"}
​
    def sorted(self):
        self.ingredients1 = list(set(self.ingredients))
        self.ingredients1.sort()
        return self.ingredients1
​
    def change_name(self):
        for i,j in enumerate(self.sorted()):
            if j[-7:] == 'berries':
                self.ingredients1[i] = j.split('berries')[0]+'berry'
        return self.ingredients1
​
    def get_cost(self):
        sum = 0
        for item in self.sorted():
            if item in self.prices.keys():
                sum += float(self.prices.get(item)[1:])
        return "{}{:.2f}".format("$",sum)
​
    def get_price(self):
        return "{}{:.2f}".format("$",float(self.get_cost()[1:]) * (1.0 + 1.5))
​
    def get_name(self):
        if len(self.change_name()) > 1:
            n1 = ""
            for n in self.change_name():
                n1 += n+" "
            return n1 + "Fusion"
        elif len(self.change_name()) == 1:
            return "{} Smoothie".format(self.change_name()[0])
        else:
            return None

