
def gimme_the_letters(s):
  L = "abcdefghijklmnopqrstuvwxyz"
  A = L[L.index(s.lower().split("-")[0]): L.index(s.lower().split("-")[1]) + 1]
  return A if s.islower() else A.upper()

