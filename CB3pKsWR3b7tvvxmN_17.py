
def is_palindrome(txt):
  txt = [i.lower() for i in txt if i.isalpha()]
  rev = txt[::-1]
  if txt == rev:
    return True
  return False

