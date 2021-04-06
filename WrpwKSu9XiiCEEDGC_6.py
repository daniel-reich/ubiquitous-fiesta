
def can_alternate(s):
  return s.count("0")==s.count("1") or s.count("0")+1==s.count("1") or s.count("0")==s.count("1")+1

