
from math import factorial
fact_of_fact=lambda n:1if n<2else fact_of_fact(n-1)*factorial(n)

