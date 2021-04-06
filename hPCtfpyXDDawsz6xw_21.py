
def verbify(txt):
  txt=txt.split()
  if txt[0].endswith('ed'):
    return " ".join(txt)
  elif txt[0].endswith('e'):
    txt=txt[0]+'d'+' '+txt[1]
    return "".join(txt)
  else:
    txt = txt[0] + 'ed'+' '+txt[1]
    return "".join(txt)

