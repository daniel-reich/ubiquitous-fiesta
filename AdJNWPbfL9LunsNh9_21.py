
def multiplication_table(n):
  output = []
  for i in range(1, n+1):
    line = [x*i for x in range(1,n+1)]
    output.append(line)
  return output

