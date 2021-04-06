
def find_cadence(chords):
  if chords[-1] == 'I':
    if chords[-2] == 'V': return 'perfect'
    if chords[-2] == 'IV': return 'plagal'
  if chords[-2] == 'V':
    return 'interrupted'
  if chords[-1] == 'V':
    return 'imperfect'
  return 'no cadence'

