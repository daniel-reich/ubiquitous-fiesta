
import enum
​
class String(enum.Enum):
  E = 1
  B = 2
  G = 3
  D = 4
  A = 5
  e = 6
def string_fret(st, fr):
  try:
    guit = String(st)
  except:
    return "Invalid input"
    
  frets = ["C", "C#/Db", "D", "D#/Eb", "E", "F", 
  "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
  
  index1 = frets.index(str(guit.name).upper())
  
  if index1 + fr < 0 or fr > 24:
    return "Invalid input"
  
  elif index1 + fr <= 11:
    return frets[index1+fr]
  
  elif index1 + fr - 11 <= 11:
    return frets[index1 + fr - 12]
  
  elif index1 + fr - 22 <= 11:
    return frets[index1 + fr - 24]

