
def string_fret(st, fr):
  if not (1 <= st <= 6) or not (0 <= fr <= 24): return 'Invalid input'
  notes = ['E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb']
  
  if st < 3:
    return notes[(fr - 5 * st + 5) % 12]
  else:
    return notes[(fr - 5 * st + 6) % 12]

