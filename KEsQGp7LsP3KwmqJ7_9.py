
def check(lst):
  for i in range(1,len(lst)):
    if lst[i:]+lst[:i] == sorted(lst):
      return 'YES'
  return 'NO'

