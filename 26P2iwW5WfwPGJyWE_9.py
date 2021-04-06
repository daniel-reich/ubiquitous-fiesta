
def possibly_perfect(key, answers):
  sames = 0
  diffs = 0
  unders = 0
  for i in range(len(key)):
    if key[i] == answers[i]:
      sames += 1
    elif key[i] == '_':
      unders += 1
    else:
      diffs += 1
  known = len(key) - unders
  if sames == known or diffs == known:
    return True
  return False

