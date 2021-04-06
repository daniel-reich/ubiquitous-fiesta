
class Clock:
​
  zero = ['111', '101', '101', '101', '111']
  one = ['010', '110', '010', '010', '111']
  two = ['111', '001', '111', '100', '111']
  three = ['111', '001', '111', '001', '111']
  four = ['101', '101', '111', '001', '001']
  five = ['111', '100', '111', '001', '111']
  six = ['100', '100', '111', '101', '111']
  seven = ['111'] + ['001'] * 4
  eight = ['111', '101', '111', '101', '111']
  nine = ['111', '101', '111', '001', '001']
  
  two_dots = ['0', '1', '0', '1', '0']
​
  def __init__(self, tme):
    self.time = tme
    
    dic = {[0,1,2,3,4,5,6,7,8,9][n]:'zero,one,two,three,four,five,six,seven,eight,nine'.split(',')[n] for n in range(10)}
    dic[':'] = 'two_dots'
​
    self.block1 = eval('Clock.{}'.format(dic[int(tme[0])]))
    self.block2 = eval('Clock.{}'.format(dic[int(tme[1])]))
    try:
      self.block3 = eval('Clock.{}'.format(dic[int(tme[2])]))
    except ValueError:
      self.block3 = eval('Clock.{}'.format(dic[tme[2]]))
    self.block4 = eval('Clock.{}'.format(dic[int(tme[3])]))
    self.block5 = eval('Clock.{}'.format(dic[int(tme[4])]))
​
    self.line1 = '0'.join([block[0] for block in [self.block1, self.block2, self.block3, self.block4, self.block5]])
    self.line2 = '0'.join([block[1] for block in [self.block1, self.block2, self.block3, self.block4, self.block5]])
    self.line3 = '0'.join([block[2] for block in [self.block1, self.block2, self.block3, self.block4, self.block5]])
    self.line4 = '0'.join([block[3] for block in [self.block1, self.block2, self.block3, self.block4, self.block5]])
    self.line5 = '0'.join([block[4] for block in [self.block1, self.block2, self.block3, self.block4, self.block5]])
​
    self.bitmap = ''.join([self.line1, self.line2, self.line3, self.line4, self.line5])
    
#c = Clock("12:13")
#print('L1 = {}'.format(c.line1 == '11100100001110111'))
#print('L2 = {}'.format(c.line2 == '10101100100010100'))
#print('L3 = {}'.format(c.line3 == '10100100001110111'))
#print('L4 = {}'.format(c.line4 == '10100100100010001'))
#print('L5 = {}'.format(c.line5 == '11101110001110111'))
​
#print(c.bitmap == '0100111000010011111000010101100001010011100001001110100100010010000111101110001110111')
​
to_bit_string = lambda t: Clock(t).bitmap

