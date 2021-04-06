
def find_cadence(chords):
  if (chords[-1]=='V'):
    return('imperfect')
  elif (chords[-1]=='I' and chords[-2]=='V'):
    return('perfect')
  elif (chords[-1]!='I' and chords[-2]=='V'):
    return('interrupted')
  elif (chords[-1]=='I' and chords[-2]=='IV'):
    return('plagal')
  else:
    return('no cadence')

