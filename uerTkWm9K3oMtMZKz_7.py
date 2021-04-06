
def sweetest_icecream(lst):
    sweet_value = {'Plain':0,'Vanilla':5,'ChocolateChip':5,'Strawberry':10,'Chocolate':10}
    return max(sweet_value[ice.flavor] + ice.num_sprinkles for ice in lst)

