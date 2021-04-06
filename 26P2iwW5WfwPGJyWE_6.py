
def possibly_perfect(key, answers):
  c = 0
  w = 0
  for i in range(len(key)):
    if key[i] != '_':
      if key[i] == answers[i]:
        c += 1
      else:
        w += 1
  if c == 0 or w == 0:
    return True
  else:
    return False

