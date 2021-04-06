
def string_fret(st, fr):
  note=['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
  start=[4,11,7,2,9,4]
  return note[(start[st-1]+fr)%12] if fr<25 and st in range(1,7) else 'Invalid input'

