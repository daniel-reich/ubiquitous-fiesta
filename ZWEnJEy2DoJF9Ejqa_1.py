
def edabit_in_string(txt):
  for x in 'edabit':
    if txt.find(x) != -1:
      txt = txt[txt.find(x):]
    else:
      return "NO"
  return "YES"

