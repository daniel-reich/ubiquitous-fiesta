
import functools
​
def gcf(num1,num2):
  factors = list(filter(lambda x: num1 % x == 0 and num2 % x == 0,range(1,num1+1)))
  return factors[-1]
def lcm(num1,num2):
  gcd = gcf(min(num1,num2),max(num1,num2))
  return (num1 // gcd) * num2
        
def lcm_of_list(numbers):
  return functools.reduce(lambda x,y: lcm(x,y),numbers)

