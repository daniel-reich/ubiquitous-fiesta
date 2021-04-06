
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
class Smoothie:
    def __init__(self, ingredients):
        self.ingredients = ingredients
​
    def get_int_cost(self):
        cost = 0
        for ingredient in self.ingredients:
            cost += float(prices[ingredient][1:])
        return round(cost, 2)
​
    def get_cost(self):
        cost = "${}".format(Smoothie.get_int_cost(self))
        if len(cost) > 4:
            return cost
        else:
            return cost + "0"
​
    def get_price(self):
        _price = "${}".format(round(Smoothie.get_int_cost(self) + Smoothie.get_int_cost(self) * 1.5, 2))
        if len(_price) > 4:
            return _price
        else:
            return _price + "0"
​
    def get_name(self):
        if len(self.ingredients) == 1:
            if self.ingredients[0].endswith("berries"):
                return "{}berry Smoothie".format(self.ingredients[0][:-7])
            else:
                return self.ingredients[0] + " Smoothie"
        else:
            s = ""
            for ingredient in sorted(self.ingredients):
                if ingredient.endswith("berries"):
                    s += "{}berry ".format(ingredient[:-7])
                else:
                    s += ingredient + " "
            s += "Fusion"
            return s

