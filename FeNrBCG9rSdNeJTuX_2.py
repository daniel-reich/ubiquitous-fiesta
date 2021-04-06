
def max_possible(n1, n2):
  n3, choices = '', sorted(str(n2))
  for i in str(n1):
    if choices and i < choices[-1]:
      n3 += choices.pop()
    else:
      n3 += i
  return int(n3)

