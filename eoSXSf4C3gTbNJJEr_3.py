
def find_cadence(chords):
  pu, ul = chords[-2:]
  if (pu, ul) == ('V', 'I'): return 'perfect'
  if (pu, ul) == ('IV', 'I'): return 'plagal'
  if pu == 'V': return 'interrupted'
  if ul == 'V': return 'imperfect'
  return 'no cadence'

