
def group_seats(lst, n):
​
  return sum(1 for x in lst for i in range(len(x)-(n-1)) if x[i:i+n] == [0] * n)

