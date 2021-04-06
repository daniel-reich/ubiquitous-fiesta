
def is_palindrome(word):
  if len(word) < 2: return True
  return word[0] == word[-1] and is_palindrome(word[1:-1])

