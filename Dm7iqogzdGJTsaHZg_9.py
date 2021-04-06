
def retrieve(txt):
  if txt=="":
    return []
  else:
    return [i.lower().strip(".") for i in txt.split(" ") if i[0].lower() in "aouieAOUIE"]

