
def emphasise(txt):
  return "".join([char.upper() if prev==" " else char.lower() for char,prev in zip(txt," "+txt)])

