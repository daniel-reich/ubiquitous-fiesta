
def possibly_perfect(key, answers):
  right = 0
  for i in range(0, len(key)):
    if key[i] == '_' or key[i] == answers[i]:
      right += 1
  return right == key.count('_') or right == len(key)

