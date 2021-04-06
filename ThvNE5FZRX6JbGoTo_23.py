
def inverter(txt, t):
  return " ".join(w[::[1,-1][t=="W"]] for w in txt.split()[::[1,-1][t=="P"]]).capitalize()

