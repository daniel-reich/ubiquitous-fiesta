
def no_duplicate_letters(phrase):
  lst = phrase.lower().split()
  
  for i in range(len(lst)):
    lst[i] = list(lst[i])
​
  for i in lst:
    if len(set(i)) != len(i):
      return False
      
  return True

