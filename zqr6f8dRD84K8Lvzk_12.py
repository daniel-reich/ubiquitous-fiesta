
# y = 3x^2 + 3x + 1
# Quadratic formula: (12y-3)**0.5 - 3 must be divisible by 6, to be valid
​
def hex_lattice(y):
  if y == 1:
    return ' o '
    
  x = ( -3 + ( 12*y - 3 ) ** 0.5 ) / 6
  
  if x%1 != 0:
    return 'Invalid'
    
  else:
    lattice = ''
    top_row = int(x+1)
    widest_row = int(2*x+1)
    
    for i in range(top_row, widest_row+1):   # top half of lattice, including widest row
      lattice += ( ' '*(widest_row - i + 1) + 'o '*i + ' '*(widest_row - i) + '\n' )
    
    for i in range(widest_row-1, top_row, -1):   # bottom half of lattice, except last
      lattice += ( ' '*(widest_row - i + 1) + 'o '*i + ' '*(widest_row - i) + '\n' )
    lattice +=  ' '*(widest_row - top_row + 1) + 'o '*top_row + ' '*(widest_row - top_row) 
  return lattice

