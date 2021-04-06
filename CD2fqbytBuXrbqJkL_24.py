
def can_build(txt1, txt2):
  l=sorted(txt2.replace(" ",""))
  return True if not False in [l.remove(i) if i in l else False for i in sorted(txt1.replace(" ",""))] else False

