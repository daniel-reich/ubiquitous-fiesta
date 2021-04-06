
def best_friend(txt, a, b):
  for x in txt.split():
    if a in x:
      if x[-1]==a or any(x[i+1]!=b for i,y in enumerate(x[:-1]) if y==a):
        return False
  return True

