
def sweetest_icecream(lst):
  sweet_dict = {'Plain' : 0, 'Vanilla' :  5, 'ChocolateChip' : 5,
          'Strawberry' : 10, 'Chocolate' : 10}
  return max([sweet_dict.get(i.flavor) + i.num_sprinkles for i in lst])

