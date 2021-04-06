
def almost_palindrome(txt):
  rev = txt[::-1]
  count = 0
  for i in range(len(txt)):
    if txt[i]==rev[i]:
      count = count + 1
  return count == len(txt)-2

