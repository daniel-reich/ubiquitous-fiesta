
def best_friend(txt, a, b):
  if txt[-1]==a:return False
  for i in range(len(txt)-1):
    if txt[i]==a and txt[i+1]!=b:
      return False
  return True

