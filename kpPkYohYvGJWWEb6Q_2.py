
def string_fret(st, fr):
  lst = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
  if st not in list(range(1,7)) or fr not in list(range(0,25)):
    return "Invalid input"
  elif st == 1:
    return lst[(4+int(fr))%12]
  elif st == 2:
    return lst[(int(fr)-1)%12]
  elif st in list(range(3,7)):
    return lst[(int(fr)+7+7*(int(st)-3))%12]

