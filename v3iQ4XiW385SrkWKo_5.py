
def check(lst):
  for i in range(len(lst)-1):
    if lst[i+1] == lst[i]:
      return True
  return False
  
def final_result(lst):
  while check(lst):
    indexes = []
    for i in range(len(lst)-1):
      char = lst[i]
      if char == lst[i+1]:
        for y in range(i, len(lst)):
          if lst[y] == char:
            indexes.append(y)
          else:
            break
        break
    for x in sorted(indexes, reverse=True):
      del lst[x]
  return lst

