
import re
​
def bifid(text):
  txt = re.sub('\W', '', re.sub('j', 'i', text.lower()))
  
  return decipher(encode(encipher(txt))) \
    if ' ' in text else \
      decipher(decode(encipher(txt)))
      
def decipher(txt):
  res = ''
  for i in re.findall('\d\d', txt):
    r, c = map(int, i)
    res += chr(ord('a')+(r-1)*5+(c-1)+(i > '24'))
  return res
  
def decode(nums):
  l = len(nums)
  return ''.join(a+b for a, b in zip(nums[:l//2], nums[l//2:]))
  
def encipher(txt):
  res = ''
  for ch in txt:
    v = 'abcdefghiklmnopqrstuvwxyz'.index(ch)
    res += '{}{}'.format(1+v//5, 1+v%5)
  return res
​
def encode(nums):
  return nums[::2]+nums[1::2]

