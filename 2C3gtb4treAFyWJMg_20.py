
def polybius(text):
  text = text.lower()
  text = text.replace("j","i").replace("'","").replace(":","")
  letters = 'abcdefghiklmnopqrstuvwxyz'
  letter_dict = {}
  for i in range(len(letters)):
    letter_dict[letters[i]]=str((((i//5)+1)*10)+((i%5)+1))
  letter_dict.update({' ':' '})
  num_dict = {letter_dict[i]:i for i in letter_dict}
  del num_dict[' ']
  num_dict.update({'  ':' '})
  if (text[0] in letters) or (text[0]=='j'):
    return ''.join([letter_dict[i] for i in text])
  else:
    text = text.replace(' ','  ')
    text = [text[i:i+2] for i in range(0,len(text),2)]
    return ''.join([num_dict[i] for i in text])

