
import math 
​
def DECIMATOR(string):
  removed_count =  math.ceil(len(string)/10);
  return string[0:-removed_count];

