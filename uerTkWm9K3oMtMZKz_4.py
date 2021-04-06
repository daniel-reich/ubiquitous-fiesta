
d = {'Plain':0,
     'Vanilla':5,
     'ChocolateChip':5,
     'Strawberry':10,
     'Chocolate':10,}
​
def sweetest_icecream(lst):
    return max([d[i.flavor] + i.num_sprinkles for i in lst])

