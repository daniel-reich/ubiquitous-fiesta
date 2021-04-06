
def min_length(lst, n):
  for i in reversed(range(len(lst))):
    for j in range(i+1):
      if sum(lst[j:j+len(lst)-i])>n: return len(lst)-i
  return -1

