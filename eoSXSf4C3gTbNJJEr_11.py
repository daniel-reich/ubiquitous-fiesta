
def find_cadence(chords):
  if chords[-1].lower() == "v": return "imperfect"
  if chords[-2].lower() == "v":
    if chords[-1].lower() == "i":
      return "perfect"
    else:
      return "interrupted"
  if chords[-2].lower() == "iv" and chords[-1].lower() == "i":
    return "plagal"
  return "no cadence"

