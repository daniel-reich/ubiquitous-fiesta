
import re
def swap_xy(txt):
  s = re.sub(r"\)\, ", ")  ", txt)
  s = re.split("  ", s)
  new_s = []
  for el in s:
    temp = re.findall(r'\-*\d+', el)
    new_s.append("(" + temp[1]+ ", "+ temp[0] + ")")
  return ", ".join(new_s)

