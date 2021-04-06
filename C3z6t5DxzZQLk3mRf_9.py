
def tune(lst):
  INTUNE = sorted([329.63, 246.94, 196, 146.83, 110, 82.41], reverse=True)
  tuner = []
  for i, string in enumerate(lst):
    offset = round((INTUNE[i]-string)/INTUNE[i], 2)
    if string == 0:
      tuner += [' - ']
    elif -.01 < offset < .01:
      tuner += ['OK']
    elif .01 <= offset < .03:
      tuner += ['>+']
    elif -.03 < offset <= -.01:
      tuner += ['+<']
    elif offset >= .03:
      tuner += ['>>+']
    elif offset <= -.03:
      tuner += ['<<+']
  return tuner

