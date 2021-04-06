
def find_cadence(chords):
    if chords[-2] == 'V':
        return 'perfect' if chords[-1] == 'I' else 'interrupted'
    if chords[-2:] == ['IV', 'I']:
        return 'plagal'
    if chords[-1] == 'V':
        return 'imperfect'
    return 'no cadence'

