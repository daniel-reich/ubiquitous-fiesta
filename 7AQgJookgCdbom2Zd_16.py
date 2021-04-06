
def pig_latin(txt):
  lc = txt[-1]
  words = txt[:-1].split()
  final = []
  vowels = ['a', 'e', 'i', 'o', 'u']
  for word in words:
    word = word.lower()
    if word[0] in vowels:
      final.append(word+'way')
    else:
      w = word[0]
      final.append(word[1:]+w+'ay')
  pigstring = " ".join(final)
  return pigstring[0].upper()+pigstring[1:]+lc

