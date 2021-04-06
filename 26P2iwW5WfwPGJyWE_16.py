
def possibly_perfect(key, answers):
  return len(set(k == a for k, a in zip(key, answers) if k != "_")) == 1

