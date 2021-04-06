
def stock_picker(lst):
  max_profit = -1
  for i in lst:
    for j in range(len(lst) - (lst.index(i) + 1)):
      if (lst[j + lst.index(i)] - i) > max_profit and (lst[j + lst.index(i)] - i) != 0:
        max_profit = (lst[j + lst.index(i)] - i)
  return max_profit

