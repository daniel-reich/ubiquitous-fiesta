
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
    def __init__(self,ingri):
        self.ingredients = ingri
        
    def get_cost(self):
        cost = 0
        for i in self.ingredients:
            cost+=float(prices[i][1:])
​
        return '$'+str(format(cost,'.2f'))
    
    def get_price(self):
        c = float(self.get_cost()[1:])
        p = c+c*1.50
        return '$'+str(format(round(p,2),'.2f'))
    def get_name(self):
        ig = self.ingredients
        for i in range(len(ig)):
            if ig[i][-3:] == "ies":
                ig[i] = ig[i][:-3] + "y"
        ig.sort()
        if len(ig)>1:
            ig.append("Fusion")
        else:
            ig.append("Smoothie")
        return " ".join(ig)

