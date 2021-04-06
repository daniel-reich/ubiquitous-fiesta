
def best_friend(txt, a, b):
  for i in range(len(txt)-1):
    if txt[i] == a:
      if txt[i+1] != b:
        return False
  if txt[-1] == a:
    return False
  return True

