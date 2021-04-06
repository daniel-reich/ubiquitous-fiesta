
import re
def markdown(symb):
  def subs(s,w):
    l = len(w)
    to_sub = " ".join("{}" if i[:l].lower()==w.lower() else i for i in s.split(" "))
    #to_sub = re.sub(r"(" + w + "|" + w.title() + "|" + w.upper() + ")[!]?",(r"{}"),s,re.I)
    occ = re.findall(r""+w+"[!\.]*",s,re.I)
    return to_sub.format(*[symb+o+symb for o in occ])
  return subs

