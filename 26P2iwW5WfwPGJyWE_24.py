
def possibly_perfect(key, answers):
  arr = []
  for i in range(len(answers)):
    if key[i] != '_':
        arr.append(key[i] == answers[i])
  if len(set(arr)) == 1:
    return True
  return False

