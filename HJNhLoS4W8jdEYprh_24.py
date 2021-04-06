
def list_between(num1, num2, lst):
  list = []
  for n in lst:
    list.append(n) if n > num1 and n < num2 else list
  return list

