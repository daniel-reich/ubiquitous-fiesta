
def cube_diagonal(volume):
  def find_sides(volume):
    return volume ** (1/3)
  def find_diag(a, b):
    return (((a ** 2) + (b ** 2)) + (a ** 2)) ** .5
  
  sides = find_sides(volume)
  
  return round(find_diag(sides, sides), 2)

