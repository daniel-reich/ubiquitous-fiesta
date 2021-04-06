
def normalize(txt):
  txt = txt.split()
  last, txt[0] = '!' if txt[-1][-1] != '.' else '', txt[0].capitalize()
  return txt[0]+' '+' '.join(txt[1:]).lower() + last

