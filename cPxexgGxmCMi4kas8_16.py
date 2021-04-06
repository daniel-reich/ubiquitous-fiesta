
class FourVector:
  def __init__(self, coord=None):
    self.coord = coord if coord else [0, 0, 0, 0]
  
  def GetComponents(self):
    return self.coord
  
  def SetComponents(self, new_coord):
    self.coord = new_coord
  
  def __add__(self, other):
    res_coord = [round(x + y, 3) for x, y in zip(self.coord, other.coord)]
    return FourVector(res_coord)
    
  def __sub__(self, other):
    res_coord = [round(x - y, 3) for x, y in zip(self.coord, other.coord)]
    return FourVector(res_coord)
    
  def __eq__(self, other):
    return all(x == y for x, y in zip(self.coord, other.coord))
    
  def __str__(self):
    return '({}, {}, {}, {})'.format(*self.coord)

