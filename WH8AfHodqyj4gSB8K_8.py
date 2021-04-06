
import re
def is_authentic_skewer(s):
  spacing = len({len(s) for s in re.findall(r"-+",s)}) == 1
  s = s.replace("-","")
  skew = bool(re.match(r"^([^AEIOU][AEIOU])*[^AEIOU]$",s))
  return skew and spacing

