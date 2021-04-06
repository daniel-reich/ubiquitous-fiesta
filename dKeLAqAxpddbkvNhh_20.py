
def group_seats(lst, n):
  return sum(sum(x[i:i+n]) == 0 for x in lst for i in range(len(x)-n+1))

