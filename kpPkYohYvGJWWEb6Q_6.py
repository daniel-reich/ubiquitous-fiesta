
def string_fret(st, fr):
  notes = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G',
            'G#/Ab', 'A', 'A#/Bb', 'B']
  dic = {1:4, 2:11, 3:7, 4:2, 5:9, 6:4}
  return notes[(dic[st]+fr)%12] if st in dic and fr<25 else 'Invalid input'

