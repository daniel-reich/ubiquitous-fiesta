
def is_first_superior(l1, l2):
  for i in range(len(l1)):
    if l1[i] > l2[i]:
      return True 
  return False

