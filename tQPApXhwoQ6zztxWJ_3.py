
import re
def get_prices(lst):
  pattern="\(\$(.+?)\)" 
  dummy_lst=[]
  for item in lst:
    op=float(re.findall(pattern,item)[0])
    dummy_lst.append(op)
    
  return dummy_lst

