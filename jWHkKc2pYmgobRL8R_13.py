
def distance_to_nearest_vowel(txt):
  vidx=[i for i in range(len(txt)) if txt[i] in 'aeiou']
  return [min([abs(c-v) for v in vidx]) for c in range(len(txt))]

