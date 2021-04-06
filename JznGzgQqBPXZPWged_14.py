
import re
def resist(net):
  def result(match):
    a,b,c = match.group(1,2,3)  
    if a == "[":
      return str(1/sum(list(map(lambda x: 1/float(x),b.split(", ")))))
    else:
      return str(sum(list(map(lambda x: float(x),b.split(", ")))))
  while True:
    if net[0].isdigit():
      return round(float(net),1)
    print(re.sub(r'(\[|\()([^\[\]\(\)]+)(\]|\))',result,net))
    net =  re.sub(r'(\[|\()([^\[\]\(\)]+)(\]|\))',result,net)

