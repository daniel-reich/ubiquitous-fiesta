
class Condi_Cypher:
​
  def __init__(self, key, shift):
    self.k = ''
    for l8r in key:
      if l8r not in self.k:
        self.k += l8r
    self.shift = shift
    for l8r in 'abcdefghijklmnopqrstuvwxyz':
      if l8r not in self.k:
        self.k += l8r
  
  def encrypt(self, msg):
​
    dic = {n+1:self.k[n] for n in range(26)}
​
    for n in range(26):
      dic[self.k[n]] = n+1
    
    num_msg = []
​
    for l8r in msg:
      try:
        num_msg.append(dic[l8r])
      except KeyError:
        num_msg.append(l8r)
    
    new_num_msg = []
​
    for num in num_msg:
      if isinstance(num, int):
        new_num = num + self.shift
        while new_num > 26:
          new_num -= 26
        new_num_msg.append(new_num)
        self.shift = num
      else:
        new_num_msg.append(num)
    
    new_msg = []
  #  print(new_num_msg)
​
    for num in new_num_msg:
      try:
        new_msg.append(dic[num])
      except KeyError:
        new_msg.append(num)
    
    return ''.join(new_msg)
​
​
def condi_cipher(msg, key, shift):
​
  CC = Condi_Cypher(key, shift)
  return CC.encrypt(msg)

