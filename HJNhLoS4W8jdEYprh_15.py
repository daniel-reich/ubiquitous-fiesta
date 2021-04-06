
def list_between(num1, num2, lst):
  thelist = []
  for i in lst:
    if num1 < i < num2:
      thelist.append(i)
    continue
  return thelist

