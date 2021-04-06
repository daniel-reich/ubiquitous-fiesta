
def letter_combinations(digits):
  p=['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
  l,comb=[''],lambda m,n:[i+j for i in m for j in n]
  for d in digits: l=comb(l,p[int(d)])
  return l

