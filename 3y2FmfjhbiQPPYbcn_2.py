
def pop(state):
  output = []
  middle = int((len(state) - 1)/2 + 1)
  reverseMiddle = int((len(state) - 1)/2)
  for i in range(middle):
    output.append(i)
  for j in reversed(range(reverseMiddle)):
    output.append(j)
  return(output)

