
class Colour_triangle:
  class Colour:
​
    def __init__(self, colour):
      self.c = colour
    
    def reproduce(self, other):
      if self.c == other.c:
        return Colour_triangle.Colour(self.c)
      else:
        if sorted([self.c, other.c]) == sorted(['R', 'G']):
          return Colour_triangle.Colour('B')
        elif sorted([self.c, other.c]) == sorted(['R', 'B']):
          return Colour_triangle.Colour('G')
        else:
          return Colour_triangle.Colour('R')
  
  def __init__(self, rawstart):
    
    self.raw = rawstart
​
    firstline = [Colour_triangle.Colour(colour) for colour in self.raw]
​
    self.triangle = {1: firstline}
​
    while min([len(i) for i in self.triangle.values()]) > 1:
      new_line = []
      new_line_ident = max(self.triangle.keys()) + 1
​
    #  print(new_line_ident)
​
      for n in range(len(self.triangle[max(self.triangle.keys())]) - 1):
        c1 = self.triangle[max(self.triangle.keys())][n]
        c2 = self.triangle[max(self.triangle.keys())][n+1]
​
        new_line.append(c1.reproduce(c2))
      
      self.triangle[new_line_ident] = new_line
​
​
def coloured_triangle(row):
​
  CT = Colour_triangle(row)
​
  return CT.triangle[max(CT.triangle.keys())][0].c

