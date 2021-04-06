
def possibly_perfect(key, answers):
  return all(key[i] == answers[i] for i in range(len(key)) if key[i].isalpha()) or all(key[i] != answers[i] for i in range(len(key)) if key[i].isalpha())

