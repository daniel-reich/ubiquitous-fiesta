
def find_cadence(ch):
  if ch[-2:] == ["V","I"]:
    return "perfect"
  elif ch[-2:] == ["IV","I"]:
    return "plagal"
  elif ch[-2] == "V":
    return "interrupted"
  elif ch[-1] == "V":
    return "imperfect"
  else:
    return "no cadence"

