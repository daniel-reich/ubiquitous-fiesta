
def find_cadence(chords):
  if chords[-2] == "V" and chords[-1] == "I":
    return "perfect"
  if chords[-2] == "IV" and chords[-1] == "I":
    return "plagal"
  if chords[-2] == "V" and chords[-1] != "I":
    return "interrupted"
  if chords[-1] == "V":
    return "imperfect"
  else:
    return "no cadence"

