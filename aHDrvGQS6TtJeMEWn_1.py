
def max_sub(lst):
  max_sum = 0
  curr_sum = 0
  for x in lst:
    curr_sum = max(0, curr_sum + x)
    max_sum = max(max_sum, curr_sum)
  return max_sum
def max_sum_pair(lst):
  max_sum = 0
  for i in range(len(lst)):
    for j in range(i,len(lst)):
      c1, c2 = max_sub(lst[i:j]), max(max_sub(lst[:i]), max_sub(lst[j:]))
      curr_sum = c1 + c2
      if curr_sum > max_sum:
        max_sum = curr_sum
  return max_sum

