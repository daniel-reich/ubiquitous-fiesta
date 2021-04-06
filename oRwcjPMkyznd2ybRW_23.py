
import functools
​
def max_product(number):
  tples  = [(num , get_digits_product(num)) for num in range(1 , number+1)];
  maximum_prod  =  max(tples , key =  lambda e : e[1])[1];
  return [e[0] for e in tples if e[1] == maximum_prod];
​
def get_digits_product(num):
  return functools.reduce(lambda a,b : a*b , get_digits(num),1);
​
def get_digits(num):
  return [int(d) for d in str(num)];

