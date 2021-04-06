
def list_between(num1, num2, lst):
  a = []
  for i in lst:
    if i > num1 and i < num2:
      a.append(i)
  return a

