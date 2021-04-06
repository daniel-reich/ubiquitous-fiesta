
def stock_picker(lst):
  mx = -1
  for a in range(len(lst)):
    for b in range(a+1,len(lst)):
      mx = max(mx,lst[b]-lst[a])
  return mx

