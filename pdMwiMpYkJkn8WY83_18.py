
def is_palindrome(word):
  if len(word) <= 1:
    return True
  else:
    if word[0] == word[len(word) - 1]:
      word = word[:-1]
      return is_palindrome(word[1:])
    else:
      return False

