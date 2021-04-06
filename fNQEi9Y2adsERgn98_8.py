
import math
def perimeter(lst):
   lst.append(lst[0])
   return round(sum([f(lst[i], lst[i+1])
           for i in range(len(lst)-1)]), 2)      
​
def f(p1, p2):
   x1, y1 = p1
   x2, y2 = p2
   return math.hypot(x2-x1, y2-y1)

