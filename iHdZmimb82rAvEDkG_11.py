
def first_even(lst):
  for i in range(len(lst)):
    if parity(lst[i]) == 0:
      return [lst[i], i]
  return False
​
def parity(n):
  return n - ((n >> 1) << 1)
​
def bitwise_index(lst):
  has_even = first_even(lst)
  if has_even == False:
    return 'No even integer found!'
  else:
    cur_largest = has_even[0]
    large_ind = has_even[1]
  for i in range(len(lst)):
    if lst[i] > cur_largest and parity(lst[i]) == 0:
      cur_largest = lst[i]
      large_ind = i
  if parity(large_ind) == 0:
    s = '@even'
  else:
    s = '@odd'
  s = s + ' index ' + str(large_ind)
  return {s:cur_largest}

