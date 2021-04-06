
import re 
​
def findShortestWords(txt):
  min=float('inf')
  words = re.findall(r"[a-z][a-z']*", txt.lower())
  for word in words: 
    if len(word) < min: 
      min = len(word)
  return [word for word in sorted(words) if len(word) == min]

