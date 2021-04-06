
def title_to_number(s):
  
  spot1 = 26**6
  spot2 = 26**5
  spot3 = 26**4
  spot4 = 26**3
  spot5 = 26**2
  spot6 = 26
  spot7 = 1
  
  alph = list('abcdefghijklmnopqrstuvwxyz'.upper())
  converter = {}
  
  for n in range(26):
    converter[alph[n]] = n+1
    
  s = [converter[l8r] for l8r in s]
​
  while len(s) < 7:
    s = [0] + s
  
  s1, s2, s3, s4, s5, s6, s7 = s
  
  total = s1*spot1 + s2*spot2 + s3*spot3 + s4*spot4 + s5*spot5 + s6*spot6 + s7*spot7
  
  return total

