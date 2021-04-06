
def find_cadence(chords):
  return "perfect" if chords[-1]=='I' and chords[-2]=='V'\
  else "plagal" if chords[-1]=='I' and chords[-2]=='IV'\
  else "imperfect"  if chords[-1]=='V'\
  else "interrupted" if chords[-1]!='I' and chords[-2]=='V'\
  else "no cadence"

