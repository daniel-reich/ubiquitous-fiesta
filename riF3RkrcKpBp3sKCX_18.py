
def cap_space(txt):
   return "".join(" "+s if s.isupper() else s for s in txt).lower()

