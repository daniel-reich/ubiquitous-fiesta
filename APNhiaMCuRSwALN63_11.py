
def almost_palindrome(txt):
  backwardIndex = -1
  invalidIndexes = []
  almostPalindrome = False
  # Obtain the indexes where the characters are not the same
  for i in range(0, len(txt) // 2):
    if txt[i] != txt[backwardIndex]:
      invalidIndexes.append((i, backwardIndex))
    backwardIndex -= 1
  # Swap the characters where the characters are not the same
  for (startingIndex, backwardIndex) in invalidIndexes:
    chars = list(txt)
    chars[backwardIndex] = chars[startingIndex]
    string = "".join(chars)
    if string == string[::-1]:
      return True
  return almostPalindrome

