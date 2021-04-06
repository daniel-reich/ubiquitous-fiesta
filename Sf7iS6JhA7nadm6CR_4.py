
class Divisibility_rule:
​
  ten_by_13 = [1, 10, 9, 12, 3, 4]
​
  def __init__(self, start):
    self.s = [start]
  
  def advance(self):
​
    number = list(reversed(str(self.s[-1])))
    nn = []
    index = 0
    for n in range(len(number)):
​
      try:
        nn.append(int(number[n]) * Divisibility_rule.ten_by_13[n])
      except IndexError:
        nn.append(int(number[n]) * Divisibility_rule.ten_by_13[index])
        index += 1
        if index >= len(Divisibility_rule.ten_by_13):
          index = 0
   #     print(index, int(number[n]), n, number, nn)
  #  print(sum(nn), self.s)
    self.s.append(sum(nn))
​
​
def divisibility_rule(n):
​
  dr = Divisibility_rule(n)
​
  while len(list(set(dr.s))) == len(dr.s):
    dr.advance()
  
  return dr.s[-1]

