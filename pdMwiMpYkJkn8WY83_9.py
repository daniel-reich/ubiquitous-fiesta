
def is_palindrome(word):
  len_word = len(word)
  if len_word == 0 or len_word == 1: return True
  elif word[0] == word[-1]: return is_palindrome(word[1:-1])
  else: return False

