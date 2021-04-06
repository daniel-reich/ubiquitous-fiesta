
def possibly_perfect(key, answers):
  everything = [key[i] == answers[i] for i in range(len(key)) if key[i] != '_']
  return all(everything) or not any(everything)

