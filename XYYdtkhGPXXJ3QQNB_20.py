
import re
​
def num_in_str(lst):
 lis = []
 for item in lst:
     res = re.search("\d+",item)
     if res:
         lis.append(item)
 return lis

