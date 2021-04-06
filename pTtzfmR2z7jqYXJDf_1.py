
def possible_palindrome(txt):
  return len([txt.count(item) for item in set(txt) if txt.count(item)%2]) <= 1

