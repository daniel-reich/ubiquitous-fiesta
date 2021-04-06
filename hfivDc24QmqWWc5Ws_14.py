
def eratosthenes(num):
  lst = list(range(2,num))
  i = 0
  while i < len(lst):
    lst = [j for j in lst if j == lst[i] or j%lst[i]]
    i += 1
  return lst

