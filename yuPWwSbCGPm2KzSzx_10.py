
Prices = {
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
        self.tot_cost = 0
    def get_cost(self):
        for el in self.ingredients: 
            self.tot_cost += float(Prices[el].replace("$",""))
            if el[-3:] == "ies":
                newEl = el[:-3] + "y"
                self.ingredients[self.ingredients.index(el)] = newEl
        self.ingredients = sorted(self.ingredients)
        return "$" + str(format(self.tot_cost,'.2f'))
    def get_price(self):
        return "$" + str(format(round(self.tot_cost * 2.5, 2),'.2f'))
    def get_name(self):
        fullName = " ".join(self.ingredients) + " Smoothie" if len(self.ingredients) < 2 else " ".join(self.ingredients) + " Fusion"
        return fullName

