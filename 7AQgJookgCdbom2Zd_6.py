
def pig_latin(txt):
  a = []
  b = txt.lower().split()
  for i in b:
      if i[0] in "aeiou":
          if b[-1]==i: a.append(i[:-1]+"way"+i[-1])
          elif b[0]==i: a.append(i.capitalize()+"way")
          else: a.append(i+"way")
      else:
          if b[-1]==i: a.append((i[1:-1].capitalize()if b[0]==b[-1]else i[1:-1])+i[0]+"ay"+i[-1])
          elif b[0]==i: a.append(i[1:].capitalize()+i[0]+"ay")
          else: a.append(i[1:]+i[0]+"ay")
  return " ".join(a)

