
def meme_sum(a, b):
  small = min(str(a),str(b),key=len)
  big = str(a) if small==str(b) else str(b)
  while len(small)<len(big):
    small = '0'+small
  final = ''
  for i,j in zip(small,big):
    final+=str(int(i)+int(j))
  return int(final)

