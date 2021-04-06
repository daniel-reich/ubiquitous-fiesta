
def best_friend(txt, a, b):
  c = []
  for i in range(len(txt)-1):
    if txt[i]==a and txt[i+1]==b: c.append(True)
    elif txt[i]==a and txt[i+1]!=b: c.append(False)
    elif txt[-1]==a: return False
  return set(c)=={True}

