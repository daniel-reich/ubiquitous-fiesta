
def best_friend(txt, a, b):
  for i in range(len(txt)):
    if txt[i]==a and (i==len(txt)-1 or txt[i+1]!=b):
      return False
  return True

