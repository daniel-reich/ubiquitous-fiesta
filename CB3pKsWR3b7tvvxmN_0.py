
def is_palindrome(txt):
  check = [s.lower() for s in txt if s.isalpha()]
  return check[::-1] == check

