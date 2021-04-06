
def min_swaps(string):
  chars = list(string)
  copy = chars[:]
  count1 = 0
  count2 = 0
  for i in range(len(string)-1):
    if chars[i] == chars[i+1]:
      count1 += 1
      if chars[i] == '1':
        chars[i+1] = '0'
      else:
        chars[i+1] = '1'
  rev = copy[::-1]
  for i in range(len(rev)-1):
    if rev[i] == rev[i+1]:
      count2 += 1
      if rev[i] == '1':
        rev[i+1] = '0'
      else:
        rev[i+1] = '1'
  if count1 <= count2:
    return count1
  else:
    return count2

