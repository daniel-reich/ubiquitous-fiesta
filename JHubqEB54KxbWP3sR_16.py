
def dist(line, x, y):
​
  class Line:
​
    def __init__(self, line):
      self.line = line
​
      line = line.split('=')
      mb = line[1].split('x')
​
      self.m = eval(mb[0])
      self.b = eval(mb[1])
​
    def distance(self, point):
​
      for_y = self.line.split('=')[1].lower()
      mb = for_y.split('x')
      for_y = '{}*x{}'.format(mb[0],mb[1])
​
      x = 0
      lp1 = [x, eval(for_y)]
      x = 10
      lp2 = [x, eval(for_y)]
​
      del x
      del for_y
​
      x1 = 0
      y1 = lp1[1]
​
      x2 = 10
      y2 = lp2[1]
​
      x0 = point[0]
      y0 = point[1]
​
      num1 = (y2 - y1) * x0
      num2 = (x2 - x1) * y0
      num3 = x2 * y1
      num4 = y2 * x1
​
      num = abs(num1 - num2 + num3 - num4)
      den = (((y2 - y1) ** 2) + ((x2 - x1) ** 2)) ** .5
​
      return round(num/den,2)
​
  line = Line(line)
​
  return line.distance([x,y])

