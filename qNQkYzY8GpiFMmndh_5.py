
import re
​
def join(lst):
  overlaps = [len(i) for i in re.findall(r'(\w+) (?=\1)', ' '.join(lst))]
  connected = re.sub(r'(\w+) (?=\1)', '', ' '.join(lst)).replace(' ', '')
  
  return [connected, min(overlaps) if overlaps else 0]

