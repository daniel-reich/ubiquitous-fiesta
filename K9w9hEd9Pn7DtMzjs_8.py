
def high_low(txt):
  lst = list(map(int, str.split(txt)))
  mn = float('inf')
  mx = float('-inf')
  for i in range(len(lst)):
    if lst[i] < mn: mn = lst[i]
    if lst[i] > mx: mx = lst[i]
  return str(mx) + " " + str(mn)

