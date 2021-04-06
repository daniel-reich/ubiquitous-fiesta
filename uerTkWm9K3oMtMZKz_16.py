
def sweetest_icecream(lst):
  sweetness_value = {"Plain":0, "Vanilla":5, "ChocolateChip":5, "Strawberry":10, "Chocolate":10}
  list = [sweetness_value[i.flavor] + i.num_sprinkles for i in lst]
  return max(list)

