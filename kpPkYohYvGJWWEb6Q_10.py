
def string_fret(st, fr):
  open_strings = ["E", "B", "G", "D", "A", "E"]
  notes = ["A", "A#/Bb", "B", "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab"]
  if st < 1 or st > 6:
    return "Invalid input"
  elif fr < 0 or fr > 24:
    return "Invalid input"
  elif (st < 1 or st > 6) and (fr < 0 or fr > 24):
    return "Invalid input"
  else:
    note = open_strings[st - 1]
    i = notes.index(note)
    for f in range(0, fr):
      i += 1
    while i >= 0:
      i -= 12
      if i >= 0 and i <= 11:
        break
    return notes[i]

