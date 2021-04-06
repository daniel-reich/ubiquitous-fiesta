
def inverter(txt, typ):
  if typ == "P":
    return " ".join(txt.split(" ")[::-1]).capitalize()
  else: 
    return " ".join(i[::-1] for i in txt.split(" ")).capitalize()

