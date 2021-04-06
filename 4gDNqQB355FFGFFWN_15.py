
def available_spots(lst, num):
  if len(lst) < 2:
    return 0
  l_wrk = []
  for i in range(len(lst)-1):
    l_wrk.append(("even" if lst[i]%2 == 0 else "odd", "even" if lst[i+1]%2 == 0 else "odd"))
  
  if num%2==0:
    return len(l_wrk) - l_wrk.count(("odd", "odd"))
  else:
    return len(l_wrk) - l_wrk.count(("even", "even"))

