
def find_cadence(chords):
  cadence = ""
  chords = chords[-2:]
  if chords[1]=="I":
    if chords[0]=="V":
      cadence="perfect"
    if chords[0]=="IV":
      cadence="plagal"
  if chords[1]=="V":
    cadence="imperfect"
  if chords[0]=="V" and chords[1]!="I":
    cadence="interrupted"
    
  if cadence=="":
    return("no cadence")
  else:
    return(cadence)

