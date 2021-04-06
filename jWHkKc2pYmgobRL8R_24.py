
def distance_to_nearest_vowel(txt):
  
  return [distance(i, s, txt) for i, s in enumerate(txt)]
  
def distance(i, s, txt):
  vowels = ("a", "e", "i", "u", "o")
  d = 0
  if s in vowels:
    return d
​
  d = len(txt)
  
  if i > 0:
    for j, _s in enumerate(txt[:i][::-1]):
      if _s in vowels:
        d = j+1
        break
  if i < len(txt):
    for j, _s in enumerate(txt[i:]):
      if _s in vowels:
        d = j if j < d else d
        break 
  return d

