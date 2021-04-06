
class Pascals_Triangle:
  
  tri = [[1], [1, 1]]
  
  def advance_to(goal):
    while len(Pascals_Triangle.tri) < goal:
      prev_row = Pascals_Triangle.tri[-1]
      curr_row = [1]
      for n in range(len(prev_row) - 1):
        cn = prev_row[n]
        nn = prev_row[n+1]
        curr_row.append(cn + nn)
      curr_row.append(1)
      Pascals_Triangle.tri.append(curr_row)
    return True
  
  def display_to(n):
    return [i for lst in Pascals_Triangle.tri[:n] for i in lst]
​
Pascals_Triangle.advance_to(28)
​
def pascals_triangle(n):
  return Pascals_Triangle.display_to(n)

