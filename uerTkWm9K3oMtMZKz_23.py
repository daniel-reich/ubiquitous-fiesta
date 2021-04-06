
def sweetest_icecream(lst):
  flavors_sweetness_dict = {'Plain': 0, 
                          'Vanilla': 5,
                          'ChocolateChip': 5,
                          'Strawberry': 10,
                          'Chocolate': 10}
  sweetness_val_lst = []
  for icecream in lst:
    total_sweetness = flavors_sweetness_dict[icecream.flavor] + icecream.num_sprinkles
    sweetness_val_lst.append(total_sweetness)
  return max(sweetness_val_lst)

