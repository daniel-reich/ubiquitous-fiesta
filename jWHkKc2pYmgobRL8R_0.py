
def distance_to_nearest_vowel(txt):
  vowel_pos = [idx for idx, i in enumerate(txt) if i in 'aeiou']
  return [min(abs(v - pos) for v in vowel_pos) for pos in range(len(txt))]

