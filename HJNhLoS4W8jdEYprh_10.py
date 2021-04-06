
def list_between(num1, num2, lst):
  new_list = []
  for value in lst:
    if value > num1 and value < num2:
      new_list.append(value)
      continue
  return new_list

