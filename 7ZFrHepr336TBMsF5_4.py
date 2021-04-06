
def percentage_changed(old, new):
  old_price = int(old[1:])
  new_price = int(new[1:])
​
  if old_price > new_price:
    pct_decrease = round((old_price - new_price) / old_price * 100)
    return "{}% decrease".format(pct_decrease)
  elif new_price > old_price:
    pct_increase = round((new_price - old_price) / old_price * 100)
    return "{}% increase".format(pct_increase)

