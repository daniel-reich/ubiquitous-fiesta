
def sort_drinks_by_price(drinks):
    sortedDrinks = sorted(drinks, key=lambda x: int(x.get('price', 0)))
    return sortedDrinks

