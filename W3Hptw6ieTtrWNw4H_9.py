
def polybius(text):
  text = text.lower()
  text = text.replace("j","i")
  text = ''.join(i for i in text if i.isalnum())
  letters = 'abcdefghiklmnopqrstuvwxyz'
  letter_dict = {}
  for i in range(len(letters)):
    letter_dict[letters[i]]=str((((i//5)+1)*10)+((i%5)+1))
  num_dict = {letter_dict[i]:i for i in letter_dict}
  if text[0] in letters:
    return ''.join(letter_dict[i] for i in text)
  else:
    text = [text[i:i+2] for i in range(0,len(text),2)]
    return ''.join(num_dict[i] for i in text)
def bifid(text):
  if ' ' in text: 
    text = polybius(text)
    text = [text[i:i+2] for i in range(0,len(text),2)]
    text = ''.join(i[0] for i in text)+''.join(i[1] for i in text)
  else:
    text = polybius(text)
    t1 = text[:len(text)//2]
    t2 = text[len(text)//2:]
    text = ''.join(t1[i]+t2[i] for i in range(len(t1)))
  return polybius(text)

