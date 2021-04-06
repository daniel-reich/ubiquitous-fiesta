
import math;
​
def salt(t):  
  result = 1+9*math.exp(-t/10);
  return round(result*1000)/1000;

