
def get_middle(word):
  n = len(word)
  if n <= 1:
    return word
  elif n % 2 == 0:
    return word[n//2-1] + word[n//2]
  else:
    return word[n//2]

