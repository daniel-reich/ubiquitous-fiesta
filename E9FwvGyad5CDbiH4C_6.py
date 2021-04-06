
def block(lst):
  return sum([(len(lst) - i - 1)*(lst[i].count(2)) for i in range(len(lst))])

