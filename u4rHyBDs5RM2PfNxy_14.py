
import re
​
def count_ones(lst):
  joined  = "".join([str(d) for d in lst]);
  mtches =  re.findall(r"1{2,}" , joined);
  return len(mtches);

