
def complete_bracelet(lst):
  lst=''.join([str(i) for i in lst])
  print(lst)
  for i in range(2,len(lst)//2+1):
    print(lst[:i])
    if lst==lst[:i]*(len(lst)//(i+1)+1): return True
  return False

