
def build_staircase(height, block):
  output = [] 
  for i in range(height):
    current_row = []
    for c in range(i+1):
      current_row.append(block)
    for c in range(i+1, height):
      current_row.append('_')
    output.append(current_row)
    
  return output

