
prices = {
    "Strawberries": 1.50,
    "Banana": 0.50,
    "Mango": 2.50,
    "Blueberries": 1.00,
    "Raspberries": 1.00,
    "Apple": 1.75,
    "Pineapple": 3.50
}
​
class Smoothie:
    def __init__(self, ingredients):
        self.ingredients = ingredients
​
    def get_cost(self):
        total_cost = []
        for e in self.ingredients:
            total_cost.append(prices.get(e))
        total_sum = sum(total_cost)
        return "$" + "{:.2f}".format(total_sum)
​
    def get_price(self):
        total_cost = []
        for e in self.ingredients:
            total_cost.append(prices.get(e))
        total_sum = float(sum(total_cost))
        return "$" + "{:.2f}".format(round(total_sum + (total_sum * 1.5), 2))
​
    def get_name(self):
        fullname = []
        for e in self.ingredients:
            if e.endswith("berries"):
                a = e.replace("berries", "berry")
                fullname.append(a)
            else:
                fullname.append(e)
        srt = sorted(fullname)
        final_name = " ".join(srt)
        if len(self.ingredients) == 1:
            return final_name + " Smoothie"
        else:
            return final_name + " Fusion"

