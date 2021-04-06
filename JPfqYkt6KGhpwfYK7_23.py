
def replace_the(txt):
  txt = txt.split()
  a = "aeuiyo"
  l = ['a' if txt[i]=='the' else txt[i] for i in range(0, len(txt))]
  return " ".join(l[k]+'n' if l[k]=='a' and l[k+1][0] in a else l[k] for k in range(0, len(l)))

