
def price_importance_sort(dct, b):
  ordered_items = sorted(
    sorted(
      dct.items(), key=lambda x: x[1]['price']
    ),
    key=lambda x: x[1]['importance'] / x[1]['price'], reverse=True
  )
  cur_budget = 0
  picks = []
  for item in ordered_items:
    name, info = item
    if cur_budget + info['price'] <= b:
      cur_budget += info['price']
      picks.append(name)
  return sorted(picks)

