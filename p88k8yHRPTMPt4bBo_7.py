
def count_vowels(txt):
  result = 0
  for letter in txt:
    if letter in "aeiouAEIOU":
      result+=1
  return result

