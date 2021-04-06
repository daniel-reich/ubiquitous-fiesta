
def bonacci(N, k):
  output = []
  one = N-1
  for i in range(k):
    if output == 0:
      output.append(0)
    elif i == one:
      output.append(1)
    else:
      output.append(sum(output[i-N:]))
  return output[k-1]

