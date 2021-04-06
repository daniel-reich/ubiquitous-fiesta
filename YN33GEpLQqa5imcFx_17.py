
def pascals_triangle(n):
  line = [1]
  for k in range(max(n,0)):             
    line.append(line[k]*(n-k)//(k+1))    
  line = [str(i) for i in line]         
  return ' '.join(line)

