
def sigilize(desire):
  desire = desire.lower()
  s= ""
  for ch in desire:
    if ch not in ["a","e","i","o","u"]:
      s+= ch
  no_reps = ""
  for ch in s[::-1]:
    if ch not in no_reps:
      no_reps += ch
  no_reps = no_reps[::-1]   
  return no_reps.upper().replace(" ","")

