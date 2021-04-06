
class Knight:
  rows = list('ABCDEFGH')
  
  def __init__(self, pos):
    self.pos = pos
    
    self.row = pos[0]
    self.rindex = Knight.rows.index(self.row)
    self.col = int(pos[1])
  
  def poss_moves(self):
    
    pms = []
    
    if self.rindex >= 2:
      if self.col >= 2:
        pms.append('{}{}'.format(Knight.rows[self.rindex - 2], self.col - 1))
      if self.col <= 7:
        pms.append('{}{}'.format(Knight.rows[self.rindex - 2], self.col + 1))
    
    if self.rindex >= 1:
      if self.col >= 3:
        pms.append('{}{}'.format(Knight.rows[self.rindex - 1], self.col - 2))
      if self.col <= 6:
        pms.append('{}{}'.format(Knight.rows[self.rindex - 1], self.col + 2))
    
    if self.rindex <= 5:
      if self.col >= 2:
        pms.append('{}{}'.format(Knight.rows[self.rindex + 2], self.col - 1))
      if self.col <= 7:
        pms.append('{}{}'.format(Knight.rows[self.rindex + 2], self.col + 1))
    
    if self.rindex <= 6:
      if self.col >= 3:
        pms.append('{}{}'.format(Knight.rows[self.rindex + 1], self.col - 2))
      if self.col <= 6:
        pms.append('{}{}'.format(Knight.rows[self.rindex + 1], self.col + 2))
    
    dic = {1: [pos for pos in pms if '1' in pos], 2: [pos for pos in pms if '2' in pos], 3: [pos for pos in pms if '3' in pos], 4: [pos for pos in pms if '4' in pos], 5: [pos for pos in pms if '5' in pos], 6: [pos for pos in pms if '6' in pos], 7: [pos for pos in pms if '7' in pos], 8: [pos for pos in pms if '8' in pos]}
    
    string = []
    
    for num in sorted(dic.keys()):
      if len(dic[num]) > 0:
        for l8r in Knight.rows:
          if '{}{}'.format(l8r,num) in dic[num]:
            string.append('{}{}'.format(l8r,num))
    
    return ','.join(string)
def knights_jump(square):
  
  return Knight(square).poss_moves()

