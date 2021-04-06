
def sweetest_icecream(lst):
    rating={'Plain':0,'Vanilla':5,'ChocolateChip':5,'Strawberry':10,'Chocolate':10}
    return max([x.num_sprinkles + rating[x.flavor] for x in lst])

