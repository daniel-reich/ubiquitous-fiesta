
def can_build(txt1, txt2):
  for l in txt1:
    if l == " ": continue
    elif l in txt2: txt2 = txt2.replace(l,"@",1)
    else: return False
  return True

