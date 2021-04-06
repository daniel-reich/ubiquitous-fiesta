
def remove_vowels(txt):
  vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  voweless = []
  
  for i in txt:
    if i not in vowel:
      voweless.append(i)
      
  return ''.join(voweless)

