
import math
​
def chemical_reactions(carbon, hydrogen, oxygen):
  ho = 0
  co = 0
  ch =0
  while oxygen >0 and hydrogen > 0 and hydrogen -2>=0 and oxygen -1 >=0:
    ho += 1
    hydrogen -=2
    oxygen -=1
  while carbon > 0 and oxygen>0 and oxygen -2>=0 and carbon -1>=0:
    co +=1
    carbon -=1
    oxygen -=2
  while carbon >0 and hydrogen>0 and carbon -1>=0 and hydrogen-4>=0:
    ch +=1
    hydrogen -= 4
    carbon -= 1
    
  return [ho, co, ch]

