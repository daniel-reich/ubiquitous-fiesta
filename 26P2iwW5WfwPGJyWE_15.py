
def possibly_perfect(key, answers):
  correct = []
  incorrect = []
  for i in range(len(key)):
    if key[i] == "_":
      correct.append(i)
      incorrect.append(i)
    else: 
      if key[i] == answers[i]:
        correct.append(i)
      else: 
        incorrect.append(i)
  if max([len(correct), len(incorrect)]) == len(key):
    return True
  return False

