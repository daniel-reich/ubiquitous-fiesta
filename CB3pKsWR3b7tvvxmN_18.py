
def is_palindrome(txt):
  c = [letter for letter in txt.lower() if letter.isalpha()]
  return c == c[::-1]

