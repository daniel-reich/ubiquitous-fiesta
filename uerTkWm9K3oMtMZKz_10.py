
def sweetest_icecream(lst):
  lst_value = []
  for ic in lst:
    if ic.flavor == "Plain":
      lst_value.append(ic.num_sprinkles)
    elif ic.flavor == "Vanilla":
      lst_value.append(5+ ic.num_sprinkles)
    elif ic.flavor == "ChocolateChip":
      lst_value.append(5+ ic.num_sprinkles)
    elif ic.flavor == "Strawberry":
      lst_value.append(10+ ic.num_sprinkles)
    elif ic.flavor == "Chocolate":
      lst_value.append(10+ ic.num_sprinkles)
  return max(lst_value)

