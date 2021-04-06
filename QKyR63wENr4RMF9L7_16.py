
def tweak_letters(txt, lst):
  return ''.join(['a' if x=='z' and y==1 else 'z' if x=='a' and y==-1 else chr(ord(x)+y) for x,y in zip(txt,lst)])

