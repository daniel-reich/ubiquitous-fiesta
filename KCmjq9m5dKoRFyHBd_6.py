
def which_side(poly, vert):
​
  class Polygon:
    
    def __init__(self, verts):
      self.verts = verts
    
    def is_reflex(self, vert):
      def area_finder(verts):
        to_add1 = []
        to_add2 = []
​
        for n in range(len(verts)):
          x1 = verts[n][0]
          y1 = verts[n][1]
          try:
            x2 = verts[n+1][0]
            y2 = verts[n+1][1]
          except IndexError:
            x2 = verts[0][0]
            y2 = verts[0][1]
​
          to_add1.append(x1*y2)
          to_add2.append(x2*y1)
        
        in_brackets = sum(to_add1) - sum(to_add2)
​
        area = in_brackets / 2
​
        return abs(area)
      
      without_vert = []
​
      for point in self.verts:
        if point != vert:
          without_vert.append(point)
      
      with_vert_area = area_finder(self.verts)
      without_vert_area = area_finder(without_vert)
​
      return without_vert_area > with_vert_area
​
  polygon = Polygon(poly)
​
  if polygon.is_reflex(vert) == True:
    return 'reflex'
  else:
    return 'regular'

