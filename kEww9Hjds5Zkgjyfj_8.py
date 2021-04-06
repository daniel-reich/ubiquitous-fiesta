
def replace_next_largest(lst):
  temp = sorted(lst)
  result = []
  for i in range(len(lst)):
    if lst[i] == max(lst):
      result.append(-1)
    else:
      a = temp.index(lst[i])
      result.append(temp[a+1])
  return result

