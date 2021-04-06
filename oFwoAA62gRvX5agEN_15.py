
from itertools import permutations
​
def knapsack(capacity, items):
  permutation_list = []
  best_item_list = []
  best_weight = 0
  best_value = 0
  content_dict = {'capacity': 0, 'items': [], 'weight': 0, 'value': 0}
  sample_item = {'name': "", 'weight': 0, 'value': 0}
  if capacity == 0:
    return content_dict
  for r in range(1,len(items)+1):
    permutation_list.extend(list(permutations(items,r)))
  print(permutation_list)
  for item_list in permutation_list:
    sum_weight = 0
    sum_value = 0
    for item in item_list:
      sum_weight += item.get('weight')
      sum_value += item.get('value')
    if sum_weight <= capacity and sum_value > best_value:
      best_item_list = item_list[:]
      best_value = sum_value[:]
      best_weight = sum_weight[:]
  content_dict = {'capacity': capacity, 'items': best_item_list, 'weight': best_weight, 'value': best_value}
  return(content_dict)

