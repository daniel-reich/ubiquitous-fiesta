
def longest_substring(digits):
  max_len = 0
  ans = ''
  for i in range(len(digits)):
    temp = digits[i]
    for x in range(i+1, len(digits)):
      if int(digits[x])%2 != int(digits[x-1])%2:
        temp += digits[x]
      else:
        break
    if len(temp) > max_len:
      max_len = len(temp)
      ans = temp
  return ans

