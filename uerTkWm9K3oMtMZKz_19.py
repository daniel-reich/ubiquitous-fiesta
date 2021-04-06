
def sweetest_icecream(lst):
  sweetness_value_dictionary = {"Plain": 0, "Vanilla": 5, "ChocolateChip": 5, "Strawberry": 10, "Chocolate":10}
  ice_cream_values = []
  for icecream in lst: 
    sweetness_value_icecream = sweetness_value_dictionary[icecream.flavor] +icecream.num_sprinkles
    ice_cream_values.append(sweetness_value_icecream)
  return max(ice_cream_values)

