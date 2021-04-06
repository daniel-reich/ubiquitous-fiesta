
def possibly_perfect(key, answers):
  rightcount = 0
  wrongcount = 0
  underscorecount = 0
  for i in range(len(key)):
    if key[i] == '_':
      underscorecount += 1
    elif key[i] == answers[i]:
      rightcount += 1
    elif key[i] != answers[i]:
      wrongcount += 1
  if rightcount+underscorecount == len(key):
    return True
  elif wrongcount+underscorecount == len(key):
    return True
  else:
    return False

