
import math
def fib_fast(num):
  listaFibo= []
  for a in range(num+1):
    Sucession = 1/math.sqrt(5)*(((1+math.sqrt(5))/2)**a-((1-math.sqrt(5))/2)**a)
    listaFibo.append(int(Sucession))
  return listaFibo[num]

