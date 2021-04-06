
def twins(lst):
  half = sum(lst) // 2 
  for i in range(len(lst)-1):
    half -= lst[i]
    if half == 0: return i+1

