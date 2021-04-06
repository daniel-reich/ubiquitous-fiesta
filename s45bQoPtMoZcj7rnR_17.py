
def closest_palindrome(num):
  numStr = str(num)
  if numStr == numStr[::-1]:
    return num
  minPalindrome = False
  minNum = num
  maxPalindrome = False
  maxNum = num
  while minPalindrome == False:
    minNum -= 1
    if str(minNum) == str(minNum)[::-1]:
      minPalindrome = True
  while maxPalindrome == False:
    maxNum += 1
    if str(maxNum) == str(maxNum)[::-1]:
      maxPalindrome = True
  if num - minNum < maxNum - num:
    return minNum
  elif num - minNum == maxNum - num:
    return minNum
  else:
    return maxNum

