
def is_undulating(n):
  n = str(n)
  first_two = n[:2]
  if len(n) < 3:
    return False
  if len(n) != 3:
    if n.count(first_two) == len(n) / 2:
      return True 
    else:
      return False 
  if len(n) == 3:
    if n[0] == n[-1]:
      return True 
    else:
      return False

