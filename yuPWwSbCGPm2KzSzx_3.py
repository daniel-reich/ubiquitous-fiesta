
prices = {
'Strawberries' : '$1.50',
'Banana' : '$0.50',
'Mango' : '$2.50',
'Blueberries' : '$1.00',
'Raspberries' : '$1.00',
'Apple' : '$1.75',
'Pineapple' : '$3.50'
}
​
class Smoothie:
    def __init__(self, ingredients):
        self.ingredients = ingredients
​
    def get_cost(self):
        # return the cost if it
        # was already calculated
        try:
            return self.cost
​
        except:
            # get the ingredients and their costs
            ingredients = self.ingredients
​
            # sum the costs
            totalCost = 0
​
            for ingredient in ingredients:
                # strip '$' and convert to float
                cost = prices[ingredient][1:]
                totalCost += float(cost)
​
            # format cost as string
            totalCost = '${0:.2f}'.format(totalCost)
​
            # create new attribute and return
            self.cost = totalCost
            return totalCost
​
    def get_price(self):
        try:
            return self.price
​
        except:
            try:
                cost = self.cost
​
            except:
                # calculate the cost
                cost = self.get_cost()
​
            # strip '$' and convert to float
            cost = float(cost[1:])
​
            # calculate the price
            price = 2.5 * cost
​
            # format price as string
            price = '${0:.2f}'.format(price)
​
            self.price = price
            return price
​
    def get_name(self):
        try:
            return self.name
​
        except:
            # sort the ingredients alphabetically
            ingredients = sorted(self.ingredients)
​
            # replace all -ies with -y
            # then join list into string
            for (i, ingredient) in enumerate(ingredients):
                ingredients[i] = ingredient.replace('ies', 'y')
​
            name = ' '.join(ingredients)
​
            # add the name suffix
            if len(ingredients) > 1:
                name += ' Fusion'
​
            else:
                name += ' Smoothie'
​
            self.name = name
            return name

