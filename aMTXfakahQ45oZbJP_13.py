
def complete_bracelet(lst):
  ln = len(lst)
  for i in range(2,ln//2 + 1):
    pattern = lst[:ln//i] 
    if ln % len(pattern):
      continue
    if all(lst[j*(ln//i):(j+1) * (ln//i)] == pattern for j in range(i)):
      return True
  
  return False

