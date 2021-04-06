
def longest_substring(digits):
  digits = digits
  longestSubstring = digits[0]
  substringArray = []
  parityBit = True if int(digits[0]) % 2 == 0 else False
  
  for x in digits[1:]:      
    if int(x) % 2 == 0 and not parityBit:
      parityBit = True
      longestSubstring += x
    elif (int(x) % 2) == 1 and parityBit:
      parityBit = False
      longestSubstring += x
    else:
      substringArray.insert(len(substringArray), longestSubstring)
      longestSubstring = x
      parityBit = True if int(x) % 2 == 0 else False
  
  if longestSubstring:
    substringArray.insert(len(substringArray), longestSubstring)
    
  return (max(substringArray, key=len))

