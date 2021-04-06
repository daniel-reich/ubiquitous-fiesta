
def GCD(lst):
  lst = sorted(lst)
  for i in range(lst[0]):
    if lst[0] % (i+1) == 0:
      temp = lst[0] / (i+1)
      for j in range(len(lst)):
        if lst[j] % temp != 0:
          break
      else: 
        return temp

