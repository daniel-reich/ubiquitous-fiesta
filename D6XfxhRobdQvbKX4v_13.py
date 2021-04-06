
def first_before_second(s, first, second):
  ind1 = []
​
  for m in enumerate(s):
      if m[1] == first:
          ind1.append(m[0])
​
  ind2 = []
​
  for m in enumerate(s):
      if m[1] == second:
          ind2.append(m[0])
​
  if max(ind1) < min(ind2):
      return True
  else:
      return False

