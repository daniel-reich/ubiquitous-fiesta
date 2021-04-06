
def neutralise(s1, s2):
  results = {"++": "+", "--": "-", "+-": "0", "-+": "0"}
  return "".join(results[x + y] for x, y in zip(s1, s2))

