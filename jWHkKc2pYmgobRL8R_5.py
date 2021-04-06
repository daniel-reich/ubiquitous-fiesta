
def distance_to_nearest_vowel(txt):
  out = []
  vowels = []
  
  for i in range(len(txt)):
    if txt[i] == "a" or txt[i] == "e" or txt[i] == "i" or txt[i] == "o" or txt[i] == "u":
      vowels.append(i)
  
  for i in range(len(txt)):
    closest = abs(i - vowels[0])
    for j in vowels:
      if abs(i - j) < closest:
        closest = abs(i - j)
    out.append(closest)
  return out

