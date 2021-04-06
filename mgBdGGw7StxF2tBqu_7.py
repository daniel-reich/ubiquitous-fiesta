
from collections import defaultdict
def duplicates(txt):
  counter = 0
  chars = defaultdict(int)
  for item in txt:
    chars[item] += 1
  for key, value in chars.items():    
    if chars[key] > 1:
      counter = counter + chars[key] - 1
  return counter

