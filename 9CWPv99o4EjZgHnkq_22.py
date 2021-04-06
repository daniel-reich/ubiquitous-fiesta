
def divide(lst, n):
  result, j = [], 0
  for i in range(1,len(lst)+1):
    if (sum(lst[j:i+1]) <= n) == False:
      result += [lst[j:i]]
      j = i
  result += [lst[j:]]
​
  return result

