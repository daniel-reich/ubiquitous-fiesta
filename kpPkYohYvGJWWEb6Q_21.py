
def string_fret(st, fr):
  notes = 'C, C#/Db, D, D#/Eb, E, F, F#/Gb, G, G#/Ab, A, A#/Bb, B'.split(', ')
  lst = [4,11,7,2,9,4]
  return notes[(lst[st-1]+fr)%12] if fr<25 and 0<st<7 else 'Invalid input'

