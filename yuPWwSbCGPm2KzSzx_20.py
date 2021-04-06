
prices = {
"Strawberries" : "$1.50",
"Banana" : "$0.50",
"Mango" : "$2.50",
"Blueberries" : "$1.00",
"Raspberries" : "$1.00",
"Apple" : "$1.75",
"Pineapple" : "$3.50"
}
​
Prices = {k: float(v.replace('$', '')) for k,v in prices.items()}
​
class Smoothie:
​
    def __init__(self, ingredients):
        self.ingredients = ingredients[:]
​
    def get_cost(self):
        cost = '$' + str(round(sum([Prices[ingredient] for ingredient in self.ingredients]), 2))
        while len(cost.split('.')[1]) < 2:
            cost += '0'
        return cost
​
    def get_price(self):
        cost = '$' + str(round(2.5 * sum([Prices[ingredient] for ingredient in self.ingredients]), 2))
        while len(cost.split('.')[1]) < 2:
            cost += '0'
        return cost
​
    def get_name(self):
        if len(self.ingredients) == 1:
            return self.ingredients[0].replace("berries", "berry") + " Smoothie"
        return ' '.join(sorted(self.ingredients)).replace("berries", "berry") + " Fusion"

