
def check_flush(table, hand):
  total = [i[-1] for i in table] + [i[-1] for i in hand]
  return any(total.count(i)>=5 for i in total)

