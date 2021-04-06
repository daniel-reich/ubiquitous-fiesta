
def knapsack(capacity, items):
  table = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]
  for i, item in enumerate(items):
    for capacity in range(1, capacity + 1):
      previous_items_value = table[i][capacity]
      if capacity >= items[i]['weight']:
        value_freeing_weight_for_item = table[i][capacity - items[i]['weight']]
        table[i+1][capacity] = max(value_freeing_weight_for_item + items[i]['value'],
                                  previous_items_value)
      else:
        table[i+1][capacity] = previous_items_value
  inserted_items = []
  capacity_left = capacity
  for i in range(len(items), 0, -1):
    if table[i-1][capacity_left] != table[i][capacity_left]:
      inserted_items.append(items[i-1])
      capacity_left -= items[i-1]['weight']
  answer = {}
  answer['capacity'] = capacity
  answer['items'] = [i for i in items if i in inserted_items]
  answer['value'] = sum([i['value'] for i in inserted_items])
  answer['weight'] = sum([i['weight'] for i in inserted_items])
  return answer

