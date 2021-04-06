
def happiness_number(s):
  smiley = s.count(':)') + s.count('(:'); sad = s.count(':(') + s.count('):')
  return smiley - sad if smiley > 0 or sad > 0 else 0

