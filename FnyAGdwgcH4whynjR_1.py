
def get_subsets(lst, n):
  result = []
  numbers = ''.join(str(i) for i in range(1, len(lst)+1))
  for i in range(1, int(numbers)):
    temp = []
    while i > 0:
      if i%10 < len(lst) and i%10 not in temp:
        temp.append(i%10)
      i = i//10
    temp2 = [lst[n] for n in temp]
    if sum(temp2) == n:
      temp2.sort()
      if temp2 not in result:
        result.append(temp2)
  unsorted = True
  while unsorted:
    unsorted = False
    for i in range(len(result)-1):
      if len(result[i]) > len(result[i+1]):
        result[i], result[i+1] = result[i+1], result[i]
        unsorted = True
      if len(result[i]) == len(result[i+1]):
        if result[i][0] > result[i+1][0]:
          result[i], result[i+1] = result[i+1], result[i]
          unsorted = True
  return result

