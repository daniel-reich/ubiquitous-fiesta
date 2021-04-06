
def distance_to_nearest_vowel(txt):
  v = [i for i in range(len(txt)) if txt[i] in 'aeiou']
  return [min([abs(i - k) for k in v]) for i in range(len(txt))]

