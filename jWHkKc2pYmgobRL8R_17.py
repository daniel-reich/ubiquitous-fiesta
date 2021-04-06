
def distance_to_nearest_vowel(txt):
  pos = [i for i,c in enumerate(txt) if c in 'aeiou']
  return [min(abs(x-i)for x in pos) for i in range(len(txt))]

