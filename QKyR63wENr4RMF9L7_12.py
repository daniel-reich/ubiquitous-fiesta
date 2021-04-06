
def tweak_letters(txt, lst):
  nlst = []
  nlst = list(map(lambda x: (ord(x)-97)%26+1, list(txt)))
  nlst = list(zip(nlst,lst))    
  return "".join(map(lambda x: chr(((x[0] + x[1]-1)%26+1)+96),nlst) )

