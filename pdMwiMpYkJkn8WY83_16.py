
def is_palindrome(word):
  return len(word) < 2 or word[0] == word[-1] and is_palindrome(word[1:-1])

