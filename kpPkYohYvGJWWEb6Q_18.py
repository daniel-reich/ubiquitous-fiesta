
notes = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
def string_fret(st, fr):
  if st not in range(1,7) or fr not in range(0, 25):
    return "Invalid input"
  else:
    if st == 1:
      start_idx = 4
    elif st == 2:
      start_idx = 11
    elif st == 3:
      start_idx = 7
    elif st == 4:
      start_idx = 2
    elif st == 5:
      start_idx = 9
    else:
      start_idx = 4
    
    note = notes[(start_idx+fr)%len(notes)]
      
  return note

