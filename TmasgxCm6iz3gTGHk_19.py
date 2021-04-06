
def min_length(lst,n):
  for i in range (len(lst)):
    for j in range (len(lst)-i+1):
      if sum(lst[j:j+i])>n:
        return i
  return len(lst) if (sum(lst)>n) else -1

