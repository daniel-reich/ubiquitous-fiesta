
def stock_picker(lst):
  profit = -1
  for i in range(len(lst)):
    for j in range(i+1,len(lst)):
      if lst[j]-lst[i]>profit:
        profit = lst[j]-lst[i]
  return profit

