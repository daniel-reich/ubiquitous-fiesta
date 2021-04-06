
def find_cadence(chords):
  if chords[-1] == "V":
    return "imperfect"
  elif chords[-1] == "I":
    if chords[-2] == "IV":
      return "plagal"
    elif chords[-2] == "V":
      return "perfect"
  elif chords [-2] == "V":
    return "interrupted"
  return "no cadence"

