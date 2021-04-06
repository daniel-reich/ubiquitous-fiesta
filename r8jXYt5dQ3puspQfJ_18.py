
def split(txt):
  vowels = []
  cons = []
  for letter in txt:
    if letter in ['a','e','i','o','u']:
      vowels.append(letter)
    else:
      cons.append(letter)
  return ''.join(vowels + cons)

