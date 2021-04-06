
from math import factorial as f
coef=lambda n,k:f(n)/(f(k)*f(n-k))
pascals_triangle=lambda n:[coef(i,k)for i in range(n)for k in range(i+1)]

