
import re
def count_eatable_chocolates(total_money, cost_of_one_chocolate):
  a=int(re.findall(r'\d\d*',total_money)[0])
  b=int(re.findall(r'[-]*\d\d*',cost_of_one_chocolate)[0])
  
  if b<1:return "Invalid Input"
  
  print(a,b)
  
  
  count=a//b
  paper=count
  
  while paper>2:
    x=paper//3
    count+=x
    paper-=x*3
    paper+=x
  
  
  
  return(count)

