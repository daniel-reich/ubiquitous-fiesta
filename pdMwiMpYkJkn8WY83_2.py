
def is_palindrome(word):
  if len(word)==0:
    return True
  else:
    if word[0]!=word[-1]:
      return False
    else:
      return is_palindrome(word[1:-1])

