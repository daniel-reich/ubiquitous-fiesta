
prices = {
    "Strawberries": "$1.50",
    "Banana": "$0.50",
    "Mango": "$2.50",
    "Blueberries": "$1.00",
    "Raspberries": "$1.00",
    "Apple": "$1.75",
    "Pineapple": "$3.50"
}
​
​
class Smoothie:
​
    def __init__(self, lst_items):
        self.ingredients = lst_items[:]
​
    def __get_cost__(self):
        return sum(float(prices[item][1:]) for item in self.ingredients)
​
    def get_cost(self):
        return '${:.2f}'.format(self.__get_cost__())
​
    def get_price(self):
        return '${:.2f}'.format(round(self.__get_cost__() * 2.5, 2))
​
    def get_name(self):
        return (' '.join(sorted(self.ingredients)).replace('berries', 'berry')
                + (' Smoothie' if len(self.ingredients) == 1 else ' Fusion'))

