
def missing_letter(txt):
  z = [ chr(ord(txt[i])-1) for i in range(1, len(txt)) if ord(txt[i])-ord(txt[i-1]) > 1 ]
  return "No Missing Letter" if not z else z[0]

