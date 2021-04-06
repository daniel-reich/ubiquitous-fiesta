
from math import factorial
def pascals_triangle(n):
 tab=[]
 for i in range(0,n):
    for j in range(0,i+1):
      x=factorial(i)/(factorial(j)*factorial(i-j))
      tab.append(x)
 return tab

