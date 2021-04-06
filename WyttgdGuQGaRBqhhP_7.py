
def min_palindrome_steps(txt):
  if isPalindrome(txt):
    return 0
  
  txt = txt[1:]
  
  return 1 + min_palindrome_steps(txt)
  
def isPalindrome(x):
  return x == x[::-1]

