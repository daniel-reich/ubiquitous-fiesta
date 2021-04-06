
notes = ["A", "A#/Bb", "B","C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab"]
​
def string_fret(st, fr):
  if st < 1 or st > 6 or fr < 0 or fr > 24:
    return "Invalid input"
  else:
    if st == 1 or st == 6:
      res = 7
    elif st == 2:
      res = 2
    elif st == 3:
      res = 10
    elif st == 4:
      res = 5
    else:
      res = 0
  return notes[(res + fr) % 12]

