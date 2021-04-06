
def knapsack(capacity, items):
  import copy
  matrix = []
  ordered_names = [item['name'] for item in items]
  values = copy.copy(items)
  values.sort(key=lambda x: (x['weight'], x['value']))
  for _ in range(len(values)):
    l = [0] * (capacity + 1)
    matrix.append(l)
​
  # algorithm starts because we have a 2d array
  # x coordinate are the weights and y are the items
  for y, row in enumerate(matrix):
    item = values[y]
    value = item['value']
    weight = item['weight']
    for x, column in enumerate(row):
      if x < 1:
        continue
      above_value = matrix[y - 1][x] if y else 0
      other_items =  matrix[y - 1][x - weight] if y - 1 >= 0 and x - weight >= 0 else 0
      matrix[y][x] = max(value + other_items, above_value)
​
  # traverse results to get the items that were selected
  y = len(matrix) - 1
  x = len(matrix[0]) - 1
  names = []
  while x >= 0 and y >= 0:
    if not matrix[y][x]:
      break
    if matrix[y][x] == matrix[y - 1][x]:
      y -= 1
      continue
    item = values[y]
    names.append(item['name'])
    y -= 1
    x -= item['weight']
  selected_items = []
  for name in ordered_names:
    if name in names:
      for item in values:
        if item['name'] == name:
          selected_items.append(item)
  total_weight = sum([item['weight'] for item in selected_items])
  value = sum([item['value'] for item in selected_items])
​
  return {'capacity': capacity, 'items': selected_items,
          'weight': total_weight, 'value': value}

