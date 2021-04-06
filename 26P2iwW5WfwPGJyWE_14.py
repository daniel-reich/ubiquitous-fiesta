
def possibly_perfect(key, answers):
  newKey = []
  newAnswers = []
  for i, v in enumerate(key):
    if v != '_':
      newKey.append(key[i])
      newAnswers.append(answers[i])
  diff = [v for i, v in enumerate(newKey) if newKey[i] != newAnswers[i]]
  same = [v for i, v in enumerate(newKey) if newKey[i] == newAnswers[i]]
  return len(diff) == 0 or len(same) == 0

