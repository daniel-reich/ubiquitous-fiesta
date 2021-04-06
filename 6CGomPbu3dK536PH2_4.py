
def accumulating_list(lst):
  result = []
​
  for i in range(len(lst)):
    if i == 0:
      result.append(lst[i])
    else:
      result.append(result[i-1]+lst[i])
​
  return result

