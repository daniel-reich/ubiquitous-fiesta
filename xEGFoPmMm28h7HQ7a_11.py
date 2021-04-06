
def combine(list1,list2):
  result = []
  for i in list1:
    for j in list2:
      result.append(i + j)
  return result
def letter_combinations(digits):
  lkp={2:['a', 'b', 'c'] , 3:['d', 'e', 'f'] , 4:['g', 'h', 'i'] , 5:['j', 'k', 'l'] 
   , 6:['m', 'n', 'o'] , 7:['p', 'q', 'r', 's'] , 8:['t', 'u', 'v'] , 9:['w', 'x', 'y', 'z']}
  lists = []
  for digit in str(digits):
    lists.append(lkp[int(digit)])
  result = lists[0]
  for idx in range(1,len(lists)):
    result = combine(result,lists[idx])
  return result

