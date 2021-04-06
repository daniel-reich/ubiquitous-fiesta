
import re
​
def space_message(txt: str) -> str:
  if '[' not in txt: return txt
  return space_message(re.sub(r'\[(\d+)([A-Z]+)\]',
    lambda m: m.group(2) * int(m.group(1)), txt, 1))

