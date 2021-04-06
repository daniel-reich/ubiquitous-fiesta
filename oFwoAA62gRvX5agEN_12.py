
def knapsack(capacity, items):
  def combine(a, b): return a[0]+b[0], a[1]+b[1]
  def solve(cap, items):
    if cap<0: return (-float('inf'), [])
    if not items: return (0, [])
    return max(combine((items[0]['value'], [items[0]]),
                       solve(cap-items[0]['weight'], items[1:])),
               solve(cap, items[1:]),
               key=lambda x: x[0])
  _, chosen = solve(capacity, items)
  return {'capacity': capacity,
          'items': chosen,
          'weight': sum(x['weight'] for x in chosen),
          'value': sum(x['value'] for x in chosen)
  }

