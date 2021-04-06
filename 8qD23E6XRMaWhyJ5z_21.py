
def happiness_number(s):
  mapping = {
    ":)": 1,
    "(:": 1,
    ":(": -1,
    "):": -1
  }
  return sum(s.count(face) * score for face, score in mapping.items())

