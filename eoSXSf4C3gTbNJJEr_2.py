
def find_cadence(chords):
  return 'perfect' if chords[-2:] == ['V','I'] else 'plagal' if chords[-2:] == ['IV','I'] else 'interrupted' if chords[-2] == 'V' else 'imperfect' if chords[-1] == 'V' else 'no cadence'

