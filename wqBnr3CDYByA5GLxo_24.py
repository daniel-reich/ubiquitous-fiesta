
import re
def unravel(txt):
  if not "[" in txt:
    return [txt]
  elif not "|" in txt:
    txt = re.sub(r'\W+',"",txt)
    return [txt]
  else:
    pairs = re.findall(r'\[[^\]]+]',txt)
    for pair in pairs:
      if not "|" in pair:
        txt = txt.replace(pair,pair[1])
    def newlist(lst,pairs):
      newlst = []
      if not pairs:
        return lst
      else:
        chars = re.findall(r'\w+',pairs[0])
        for el in lst:
          for i in range(0,len(chars)):
            newlst.append(el.replace(pairs[0],chars[i]))
        pairs.pop(0)
        return newlist(newlst,pairs)
    return sorted(newlist([txt],pairs))

