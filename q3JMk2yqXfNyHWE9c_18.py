
def double_letters(word):
  a = list(word)
  n = len(word)
  for i in range(0,n-1):
    if a[i]==a[i+1]:
      return True
      exit
  return False

