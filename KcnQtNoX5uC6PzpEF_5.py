
def check_sum(lst, n):
  for i in range(len(lst)):
    for j in range(len(lst)):
      if i != j:
        total = lst[i] + lst[j]
        if total == n:
          return True
  
  else:
    return False

