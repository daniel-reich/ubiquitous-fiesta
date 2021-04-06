
def super_reduced_string(txt):
  if not txt: return "Empty String"
  a = "abcdefghijklmnopqrstuvwxyz"
  b = [i * 2 for i in a]
  while any(i in txt for i in b):
        for i in b:
            if i in txt:
               txt = txt.replace(i, "")
  return "Empty String" if not txt else txt

