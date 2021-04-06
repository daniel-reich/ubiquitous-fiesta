
class Rail_Cypher:
​
  
  def __init__(self, rail_num):
    self.rn = rail_num
    self.rails = {n: [] for n in range(self.rn)}
  
  def encrypt(self, msg):
​
    rail = 0
    direct = 'U'
    msg = list(msg)
​
    while len(msg) > 0:
     # print(msg, rail, direct)
      self.rails[rail].append(msg.pop(0))
      if direct == 'U':
        if rail == max(self.rails.keys()):
          direct = 'D'
          rail -= 1
        else:
          rail += 1
      elif direct == 'D':
        if rail == 0:
          direct = 'U'
          rail += 1
        else:
          rail -= 1
    
    return ''.join([''.join(self.rails[rail]) for rail in sorted(self.rails.keys())])
​
def rail_fence_cipher(msg, rails):
​
  rc = Rail_Cypher(rails)
  return rc.encrypt(msg)

