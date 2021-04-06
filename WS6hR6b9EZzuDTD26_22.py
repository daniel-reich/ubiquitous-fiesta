
def no_duplicate_letters(phrase):
  p=phrase.split()
  result=0
  for i in range(len(p)):
    if len(p[i])==len(set(p[i])): result+=1
  if result== len(p): return True
  else: return False

