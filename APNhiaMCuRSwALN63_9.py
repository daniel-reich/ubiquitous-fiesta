
def almost_palindrome(txt):
  length = len(txt)
  mismatches = 0
  for i in range(len(txt)//2+1):
    if txt[i] != txt[length-i-1]:
      mismatches += 1
  return mismatches == 1

