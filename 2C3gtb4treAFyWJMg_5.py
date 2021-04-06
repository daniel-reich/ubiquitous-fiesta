
import re
​
def polybius(txt):
  txt = re.sub('[^\w\s]', '', re.sub('j', 'i', txt.lower()))
  
  return re.sub('\d\d', lambda x: decipher(x.group(0)), txt) \
    if txt[0].isdigit() else \
      re.sub('\w', lambda x: encipher(x.group(0)), txt)
      
def decipher(num):
  r, c = map(int, num)
  return chr(ord('a')+(r-1)*5+(c-1)+(num > '24'))
  
def encipher(ch):
  v = 'abcdefghiklmnopqrstuvwxyz'.index(ch)
  return '{}{}'.format(1+v//5, 1+v%5)

