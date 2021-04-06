
def sweetest_icecream(lst):
    sw = {"Plain": 0, "Vanilla": 5, "ChocolateChip": 5, "Strawberry": 10, "Chocolate": 10}
    return max(sw[i.flavor] + i.num_sprinkles for i in lst)

