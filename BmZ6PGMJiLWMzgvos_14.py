
def is_special_array(lst):
  for i in range(len(lst)+1):
    if lst[i-1] %2 != 0 and i%2!=0:
      return False
    elif lst[i-1] %2 == 0 and i%2==0:
      return False
  return True

