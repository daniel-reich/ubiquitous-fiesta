
def final_result(lst):
  while True:
    if len(lst) <= 1:
      return lst
    for i in range(len(lst)):
      if i == len(lst)-1:
        return lst
      if lst[i] == lst[i+1]:
        break
    lst = lst[:i] + list("".join(lst[i:]).lstrip(lst[i]))
  return lst

