
def pig_latin(txt):
  lw=txt[-1]
  return (" ".join([i[1:]+i[0]+"ay" if not i[0] in "aeiou" else i+"way" for i in txt.replace(lw,"").lower().split()])+lw).capitalize()

