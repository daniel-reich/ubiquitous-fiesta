
def is_palindrome(word):
  if not word:
    return True
  return is_palindrome(word[1:-1]) if word[0] == word[-1] else False

