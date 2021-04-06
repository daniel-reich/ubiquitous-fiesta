
def count_repetitions(lst):
  inverse = dict()
  emp_l = []
  for k in lst:
    if k not in emp_l:
      emp_l.append(k)
      inverse[k] = lst.count(k)
​
  return inverse

