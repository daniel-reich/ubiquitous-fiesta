
def vigenere(txt,key):
  if " " in txt:
    txt = [i.upper() for i in txt if i.isalpha()]
    return "".join([chr((ord(txt[i])+ord(key[i%len(key)])-162)%26+65) for i in range (len(txt))])
  return "".join([chr((ord(txt[i])-ord(key[i%len(key)])+162)%26+65) for i in range (len(txt))])

