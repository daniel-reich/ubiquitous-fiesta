
def longest_substring(num):
  firstDigit = int(num[0]) % 2 == 0
  index = 1; cut = 0
  longest = ""
  
  while index < len(num):
    currentDigit = int(num[index]) % 2 == 0
    
    if currentDigit == firstDigit:
      newNum = num[cut : index]
      longest = newNum if len(newNum) > len(longest) else longest
      cut = index
    elif index == len(num) - 1:
      longest = num[cut:len(num)] if len(num[cut:len(num)]) > len(longest) else longest
      
    firstDigit = currentDigit
    index += 1
  
  return longest

