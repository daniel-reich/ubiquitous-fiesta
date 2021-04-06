
def complete_bracelet(lst):
  if len(set(lst)) == 1:
    return False
  a = 2
  while a <= (len(lst)+1)//2:
    if any([lst == lst[:a]*i for i in range(len(lst)//2 + 1)]):
      return True 
    a += 1
  return False

