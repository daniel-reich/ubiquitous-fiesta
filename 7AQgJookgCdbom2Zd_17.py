
VOWELS = ['a','e','i','o','u']
def pig_latin(txt):
  pig = []
  for word in txt.split():
    tmp = ""
    pun = " "
    if not word[-1].isalpha():
      pun = word[-1] 
      word = word[:-1]
    if word[0].lower() not in VOWELS:
      tmp = word[1:] + word[0].lower() + 'ay' 
    else: 
      tmp = word + 'way'
    if word[0].isupper():
      tmp = tmp[0].upper() + tmp[1:]
    pig += [tmp] + [pun]
  return "".join(pig)

