
def atbash(txt):
  uc,lc = list(range(ord('A'), ord('Z')+1)), list(range(ord('a'), ord('z')+1))
  normal = [chr(i) for i in uc]+[chr(i) for i in lc]
  cipher = [chr(i) for i in uc[::-1]]+[chr(i) for i in lc[::-1]]
  return ''.join(cipher[normal.index(i)] if i.isalpha() else i for i in txt)

