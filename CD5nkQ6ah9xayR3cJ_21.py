
def add_odd_to_n(num):
  sum_lst = []
  for x in range(0, num+1):
    if x % 2 != 0:
      sum_lst.append(x)
  return sum(sum_lst)

