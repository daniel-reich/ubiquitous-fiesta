
def find_a_seat(n, lst):
  num = [i for i in lst if i <= n / (len(lst) * 2)]
  return lst.index(num[0]) if num else -1

