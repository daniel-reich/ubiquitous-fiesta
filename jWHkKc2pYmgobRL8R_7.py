
def distance_to_nearest_vowel(txt):
  result = []
  vowels = [i for i,letter in enumerate(txt) if letter in "aeiou"]
  for i in range(len(txt)):
    result.append(min(map(lambda x: abs(i-x), vowels)))
  return result

