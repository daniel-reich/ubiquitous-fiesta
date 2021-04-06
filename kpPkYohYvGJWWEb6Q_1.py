
def string_fret(st, fr):
  notes=['E','F','F#/Gb','G','G#/Ab','A','A#/Bb','B','C','C#/Db','D','D#/Eb']
  return 0<st<7 and 0<=fr<25 and notes[((st-1)%5*7+fr+1*(2<st<6))%12] or 'Invalid input'

