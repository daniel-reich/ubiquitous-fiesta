
def alphabet_index(txt):
  import string
  strin = string.ascii_lowercase
  txt = txt.lower()
  txt_new = []
  for i in txt:
    if i in strin:
      txt_new.append(str(strin.index(i)+1))
  return " ".join(txt_new)

