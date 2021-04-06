
def longest_substring(digits):
  lst = []
  alt = digits[0]
  for i in range(1, len(digits)):
    if int(digits[i]) % 2 != int(digits[i-1]) % 2:
      alt += digits[i]
    else:
      lst.append(alt)
      alt = digits[i]
    lst.append(alt)
  return max(lst, key = len)

