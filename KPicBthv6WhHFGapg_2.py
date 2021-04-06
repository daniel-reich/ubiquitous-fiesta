
def count_syllables(txt):
  syllables = ['a', 'e', 'i', 'o', 'u']
  counter = 0
  
  for char in txt.lower():
    if char in syllables:
      counter += 1
      
  return counter

