
def count_vowels(txt):
  count = 0
  a = txt.lower()
  #b = list(a)
  for values in a:
    if (values == 'a' or values == 'e' or values == 'i' or values == 'o'or values == 'u'):
      count+=1
  return count

