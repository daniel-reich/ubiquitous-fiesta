
def simple_encoder(s):
  s=s.lower()
  word=[]
  for letter in s:
    counter=s.count(letter)
    if counter == 1:
      letter='['
      word.append(letter)
    else:
      letter=']'
      word.append(letter)
  return ''.join(word)

