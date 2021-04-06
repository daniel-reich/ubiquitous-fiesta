
def secret(txt):
​
  sp = txt.split('.')
  hdr = "<"+sp[0]+" class='"
  ftr = "'></"+sp[0]+">"
  
  mid = " ".join(sp[1:])
  
  return (hdr+mid+ftr)

