
def fibonacci(num):
 n1=1;n2=2;i=0;
 while i < num-1:
​
  nth = n1 + n2
  n1 = n2
  n2 = nth
  i += 1
 return n1

