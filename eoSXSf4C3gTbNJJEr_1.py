
def find_cadence(chords):
  if chords[-2:] == ["V", "I"]: return "perfect"
  if chords[-2:] == ["IV", "I"]: return "plagal"
  if chords[-2] == "V": return "interrupted"
  if chords[-1] == "V": return "imperfect"
  return "no cadence"

