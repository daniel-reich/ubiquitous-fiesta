
def flip(txt, spec):
  if spec=="word":
    return " ".join([x[::-1] for x in txt.split(" ")])
  if spec=="sentence":
    return " ".join(reversed(txt.split(" ")))

