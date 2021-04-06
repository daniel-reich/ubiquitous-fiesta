
def is_vowel_sandwich(s):
  vowels = ['a','e','i','o','u']
  if len(s) == 3:
    if s[0] not in vowels and s[1] in vowels and s[2] not in vowels :
      return True
    else:
      return False
  else: 
    return False

