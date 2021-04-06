
def is_palindrome(t):
  t=list(map(str.lower,filter(str.isalpha,t)))
  return t==t[::-1]

