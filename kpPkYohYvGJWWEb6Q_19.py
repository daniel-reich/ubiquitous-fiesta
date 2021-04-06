
def string_fret(st, fr):
  if (st<1 or st > 6) or fr > 24:
    return 'Invalid input'
  chromatic = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
  string = ['E','B','G','D','A','E']
  for note in chromatic:
    if string[st-1] == note:
      note_index = chromatic.index(note) + fr
      while note_index >= 12:
        note_index -=12
      return chromatic[note_index]
      break

