
import re
def add_bill(money):
  return sum(int(d[:-1])*1000 if "k" in d else int(d) for d in 
    re.findall(r"d(\w+)", money))

