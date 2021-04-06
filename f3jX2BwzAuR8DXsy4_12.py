
from math import factorial as f
def fact_of_fact(n):
  return eval("*".join(map(lambda x:str(f(x)),range(1,n+1))))

