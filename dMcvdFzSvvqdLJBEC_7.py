
def num_of_days(cost, savings, start):
  required = cost - savings
  l = []
  while sum(l) < required:
    l.append(start)
    start += 1
    if len(l)%7==0:
      start = l[-7]+1
  return len(l)

