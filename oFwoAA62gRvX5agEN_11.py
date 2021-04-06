
def knapsack(capacity, items):
  if capacity == 0:
      return {'capacity':0, 'items':[], 'weight':0, 'value':0}
  value = {}
  for weight in range(1, capacity+1):
      for item in items:
          diff = weight - item['weight']
          if diff == 0:
              if item['value'] > value.get(weight, {}).get('value', 0):
                  value[weight] = {'items':[item], 'value':item['value']}
          elif diff in value:
              prev = value[diff]['items']
              val = value[diff]['value']
              if item in prev:
                  continue
              if item['value'] + val > value.get(weight, {}).get('value', 0):
                  value[weight] = {'items':prev + [item], 'value': val + item['value']}
  cap = max(value, key=lambda x:value[x]['value'])
  res = {'weight': cap, 'value':value[cap]['value'], 'capacity': capacity}
  res['items'] = sorted(value[cap]['items'], key=items.index)
  return res

