
def pig_latin(txt):
  vowels = ['a','e','i','o','u']
  return ' '.join((word[1:] + word[:1] + 'ay') if word[0].lower() not in vowels else (word + 'way') for word in txt[:-1].split()).capitalize() + txt[-1:]

