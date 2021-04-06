
def multiply(n1, n2):
  final = 0
  for i in range(abs(n2)):
    final+=n1
  return abs(final) if n1<0 and n2<0 or n1>0 and n2>0 else -abs(final)

