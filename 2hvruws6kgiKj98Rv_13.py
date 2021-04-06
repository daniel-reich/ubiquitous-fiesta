
def to_scottish_screaming(txt):
  txt = txt.upper()
  srr = ""
  for i in range(len(txt)):
    if txt[i] in ['A','I','O','U']:
      srr += 'E'
    else:
      srr += txt[i]
  return srr

