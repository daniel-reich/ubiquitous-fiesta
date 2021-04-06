
def split(txt):
  #use a counter to close off clusters
  # increase for each (, decrease for each )
  # once hits zero then mark the starting and closing index and move
  # the cluster to the output list
  
  start = 0
  counter = 0
  output = []
  for i in range(len(txt)):
    if txt[i] == '(':
      counter += 1
    else:
      counter -= 1
      
    if counter == 0:
      output.append(txt[start:i+1])
      start = i + 1
  
  return output

