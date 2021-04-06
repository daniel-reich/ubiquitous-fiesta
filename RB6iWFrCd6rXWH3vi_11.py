
def longest_substring(digits):
  digits = [int(i) for i in digits]
  res, temp = [], [digits[0]]
​
  i = 1
  while i < len(digits):
    if digits[i]%2 != digits[i-1]%2:
      temp.append(digits[i])
    else:
      if len(temp) > len(res):
        res = temp
      temp = [digits[i]]
    i += 1
  if len(temp) > len(res):
    res = temp
  return ''.join(str(i) for i in res)

