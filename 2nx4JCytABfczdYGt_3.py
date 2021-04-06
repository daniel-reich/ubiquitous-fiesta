
def conjugate(verb, pronoun):
  P={
    1:["Io","o"],
    2:["Tu","i"],
    3:["Egli","a"],
    4:["Noi","iamo"],
    5:["Voi","ate"],
    6:["Essi","ano"]
  }
  r=verb[:-3]
  if r.endswith("c") or r.endswith("g"):
    return "{} {}h{}".format(P[pronoun][0],r,P[pronoun][1])
  elif r.endswith("i"):
    if pronoun==2 or pronoun==4:
      return "{} {}{}".format(P[pronoun][0],r[:-1],P[pronoun][1])
  return "{} {}{}".format(P[pronoun][0],r,P[pronoun][1])

