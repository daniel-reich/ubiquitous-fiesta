
def find_cadence(chords):
  if chords[-1]=="V":
    return ('imperfect')
  elif chords[-2]=="V" and chords[-1]=="I":
    return ('perfect')
  elif chords[-2]=="V" and chords[-1]!="I":
    return ('interrupted')
  elif chords[-2]=="IV" and chords[-1]=="I":
    return ('plagal')
  else:
    return "no cadence"

