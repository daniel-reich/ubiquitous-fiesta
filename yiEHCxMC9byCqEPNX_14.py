
from string import ascii_lowercase as al
def is_palindrome(p):
  sanitize = ""
  for letter in p.lower():
    if letter in al:
      sanitize += letter
  if len(sanitize) < 2:
    return True
  return sanitize[0] == sanitize[-1] and is_palindrome(sanitize[1:-1])

