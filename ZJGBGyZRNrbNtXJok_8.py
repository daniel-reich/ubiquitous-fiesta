
def nearest_vowel(s):
  for i in range(13):
    if chr(ord(s)-i) in 'aeiou': 
      return chr(ord(s)-i)
    if chr(ord(s)+i) in 'aeiou': 
      return chr(ord(s)+i)

