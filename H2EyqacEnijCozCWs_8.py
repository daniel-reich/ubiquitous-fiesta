
def first_n_vowels(s, x):
  vowels = "aeiou"
  lst = [i for i in s if i in vowels]
  if x > len(lst):
    return "invalid"
  return"".join((lst[:x]))

