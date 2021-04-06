
def list_between(num1, num2, lst):
  k = []
  for i in lst:
    if i > num1 and i < num2:
      k.append(i)
  return k

