
def remove_vowels(txt):
  vowels = ['a', 'e', 'i', 'o', 'u']
  return ''.join([character for character in txt if character.lower() not in vowels])

