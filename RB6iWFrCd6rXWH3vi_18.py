
def longest_substring(digits):
  last = 0
  longest = ""
  current = ""
  for i in digits:
    if (int(i) % 2 == 0 and int(last) % 2 == 0) or (int(i) % 2 != 0 and int(last) % 2 != 0):
      if len(current) > len(longest):
        longest = current
      current = i
      last = i
    else: 
      current += i
      last = i
  if len(current) > len(longest):
    longest = current
  return longest

