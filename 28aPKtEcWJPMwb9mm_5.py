
class Base:
​
  def __init__(self, base):
    self.b = base
  
  def convert_from_int(self, inte):
​
    nums = [1]
    expo = 1
​
    while max(nums) < inte:
      nums.append(self.b**expo)
      expo += 1
    
    nums = list(reversed(nums))
​
    new_num = []
​
    for num in nums:
      if num <= inte:
        new_num.append(inte // num)
        inte = inte % num
      else:
        new_num.append(0)
    
    return int(''.join([str(i) for i in new_num]))
​
b2 = Base(2)
​
​
def modify(txt):
  
  txt = ''.join(list(reversed(txt))).lower()
​
  a = 'abcdefghijklmnopqrstuvwxyz'
  
  txt_nums = int(''.join([str(a.index(l8r) + 1) for l8r in txt]))
  
  return b2.convert_from_int(txt_nums)

