
vowels = ["a", "e", "i", "o", "u"]
​
def distance_to_nearest_vowel(txt):
  res = []
  vow = []
  for i in range(len(txt)):
    c = txt[i]
    res.append(0 if c in vowels else -1)
    if c in vowels: vow.append(i)
  for i in range(len(res)):
    if res[i] == -1:
      min = float("inf")
      for v in vow:
        if abs(i - v) < min:
          min = abs(i - v)
      res[i] = min
  return res

