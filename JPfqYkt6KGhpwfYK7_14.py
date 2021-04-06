
def replace_the(txt):
  tsp = (txt+ " *").split(" ")
  return " ".join([(tsp[i] if tsp[i] != "the" else "an" if tsp[i+1][0] in "aeiou" else "a") for i in range(len(tsp)-1)])

