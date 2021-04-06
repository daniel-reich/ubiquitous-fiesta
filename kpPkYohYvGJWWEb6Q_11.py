
def string_fret(st, fr):
  if st == 0 or st > 6 or fr < 0 or fr > 24:
    return 'Invalid input'
  notes = ['E','F','F#/Gb','G','G#/Ab','A','A#/Bb','B','C','C#/Db','D','D#/Eb']
  if (st == 1) or (st == 6):
    note = notes + notes
    note.append(notes[0])
    return note[fr]
  if st == 2:
    notea, noteb = notes[:7], notes[7:]
    note = noteb + notes + notea
    note.append(noteb[0])
    return note[fr]
  if st == 3:
    notea, noteb = notes[:3], notes[3:]
    note = noteb + notes + notea
    note.append(noteb[0])
    return note[fr]
  if st == 4:
    notea, noteb = notes[:10], notes[10:]
    note = noteb + notes + notea
    note.append(noteb[0])
    return note[fr]
  if st == 5:
    notea, noteb = notes[:5], notes[5:]
    note = noteb + notes + notea
    note.append(noteb[0])
    return note[fr]

