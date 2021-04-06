
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
    ingredientlist = []
    cost = 0
    taxcost = 0
    strcost = ''
    finalsentence = ''
    
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.ingredientlist = ingredients
    
    def get_cost(self):
        for i in range(0, len(self.ingredientlist)):
            self.cost = self.cost + float(prices[self.ingredientlist[i]][1 : ])
        self.strcost = str(self.cost * 1.5)
        return "${:,.2f}".format(self.cost)
        
    def get_price(self):
        if str(self.cost * 1.5)[-2] != '.' and str(self.cost * 1.5)[-3] != '.' and str(self.cost * 1.5)[list(str(self.cost * 1.5)).index('.') + 3] == '5':
            self.cost = self.cost + round((self.cost * 1.5) + 0.001, 2)
        else:
            self.cost = self.cost + round(self.cost * 1.5, 2)
        return "${:,.2f}".format(self.cost)
        
    def get_name(self):
        self.ingredientlist.sort()
​
        for i in range(0, len(self.ingredientlist)):
            if self.ingredientlist[i] == "Blueberries":
                self.finalsentence = self.finalsentence + "Blueberry "
            elif self.ingredientlist[i] == "Raspberries":
                self.finalsentence = self.finalsentence + "Raspberry "
            elif self.ingredientlist[i] == "Strawberries":
                self.finalsentence = self.finalsentence + "Strawberry "
            else:
                self.finalsentence = self.finalsentence + self.ingredientlist[i] + ' '
        if len(self.ingredientlist) == 1:
            self.finalsentence = self.finalsentence + "Smoothie"
        else:
            self.finalsentence = self.finalsentence + "Fusion"
        return self.finalsentence

