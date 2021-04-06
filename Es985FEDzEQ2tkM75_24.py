
import string
import re
def caesar_cipher(s, k):
  newS = "" 
  for i in range(len(s)):  
    val = ord(s[i])  
    dup = k  
    if val + k>122:  
      k -= (122-val)
      k = k % 26
      newS += chr(96 + k)  
    else:
      newS += chr(val + k)  
    k = dup
  chars = re.escape(string.punctuation)
  return re.sub(r'['+chars+']', ' ',newS)

