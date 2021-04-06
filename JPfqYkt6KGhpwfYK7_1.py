
def replace_the(n):
  n = n.lower().split()
  return' '.join('an'if n[i]=='the'and n[i+1][0]in'aeiou'else'a'if n[i]=='the'and n[i+1][0]not in'aeiou'else n[i]for i in range(len(n)))

