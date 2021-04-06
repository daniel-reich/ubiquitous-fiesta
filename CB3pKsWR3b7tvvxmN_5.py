
def is_palindrome(txt):
  s = ""
  for l in txt.lower():
    if l.isalpha():
      s+=l
  return s==s[::-1]

