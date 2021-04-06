
def inverter(txt, type):
  if type=="P": return " ".join([w for w in txt.lower().split()][::-1]).capitalize()
  return " ".join(w[::-1] for w in txt.lower().split()).capitalize()

