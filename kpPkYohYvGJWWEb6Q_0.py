
def string_fret(st, fr):
  notes = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
  strings = {6:'E', 5:'A', 4:'D', 3:'G', 2:'B', 1:'E'}
  if st not in range(1,7) or fr > 24:
    return 'Invalid input'
  return notes[(notes.index(strings[st]) + fr)%12]

