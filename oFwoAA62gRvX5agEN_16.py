
def knapsack(capacity, items):
  def ks(n, c): 
    if n < 0 or c == 0:
      result = 0 
    elif items[n]['weight'] > c:
      result = ks(n-1, c)
    else:
      tmp1 = ks(n-1, c)
      tmp2 = items[n]['value'] + ks(n-1, c - items[n]['weight'])
      result = max(tmp2, tmp1)
    return result
​
  def lt(idx, cap, val):
    if val == 0 or cap == 0 or idx < 0:
      return []
    elif items[idx]['value'] > val:
      return lt(idx-1, cap, val)
    elif items[idx]['weight'] > cap:
      return lt(idx-1, cap, val)
    else:
      return min(lt(idx-1, cap, val), [items[idx]] + lt(idx-1, cap-items[idx]['weight'], val-items[idx]['value']), key = lambda x: val- sum(it['value'] for it in x))
​
  i = len(items)-1
  value = ks(i, capacity)
  items_list = lt(i, capacity, value)
  sorted_items_list = [item for item in items if item in items_list]
  weight = sum(item['weight'] for item in sorted_items_list)
  return {'capacity': capacity, 'items': sorted_items_list, 'weight': weight, 'value': value}

