
class Cipher:
​
  l8rs = 'abcdefghijklmnopqrstuvwxyz'
​
  def __init__(self, keyword):
    self.k = []
​
    for l8r in keyword:
      if l8r not in self.k:
        self.k.append(l8r)
​
    self.new_alph = ''.join(self.k + [l8r for l8r in Cipher.l8rs if l8r not in keyword])
​
    self.encrypt_dic = {Cipher.l8rs[n]: self.new_alph[n] for n in range(26)}
    self.decrypt_dic = {self.new_alph[n]: Cipher.l8rs[n] for n in range(26)}
​
  def encrypt(self, msg):
    try:
      return ''.join([self.encrypt_dic[l8r] for l8r in msg])
    except KeyError:
      tr = []
​
      for l8r in msg:
        try:
          tr.append(self.encrypt_dic[l8r])
        except KeyError:
          tr.append(l8r)
      
      return ''.join(tr)
  
  def decrypt(self, msg):
    try:
      return ''.join([self.decrypt_dic[l8r] for l8r in msg])
    except KeyError:
      tr = []
​
      for l8r in msg:
        try:
          tr.append(self.decrypt_dic[l8r])
        except KeyError:
          tr.append(l8r)
        
      return ''.join(tr)
​
​
​
def keyword_cipher(key, msg):
​
  cipher = Cipher(key)
​
  return cipher.encrypt(msg)

