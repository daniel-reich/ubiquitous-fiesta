
def multiplicity(lst):
  counted = []
  m = []
  for num in lst:
    if num not in counted:
      m.append([num, lst.count(num)])
      counted.append(num)
  return m

