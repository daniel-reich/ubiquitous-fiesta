
def best_friend(txt, a, b):
  answer = True
  for i in range(len(txt)):
    if txt[i] == a:
      try:
        if txt[i+1] and txt[i+1] == b:
          answer = True
        else:
          return False
      except IndexError:
        return False
  return answer

