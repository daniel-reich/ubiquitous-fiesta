
def collect(s, n):
  if len(s)< n:
    return []
  output= []
  while len(s) > 0:
    output.append(s[:n])
    s = s[n:]
  if len(output[-1]) < n:
    output = output[:-1]
  return sorted(output)

