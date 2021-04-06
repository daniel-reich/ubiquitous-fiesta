
def count_vowels(txt):
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  count = 0  
  for l in txt:
    if l in vowels:
      count += 1
  return count

