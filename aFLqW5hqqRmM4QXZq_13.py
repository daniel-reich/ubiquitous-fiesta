
def bar_chart(results):
  lst = []
  for i in ["Q1", "Q2", "Q3", "Q4"]:
    lst.append(Quarter(i, results[i]))
  lst.sort()
  lst.reverse()
  ret = []
  for i in lst:
    if i.result == 0:
      ret.append(i.name+"|"+"#"*(i.result//50)+str(i.result))
    else:
      ret.append(i.name+"|"+"#"*(i.result//50)+" "+str(i.result))
  return "\n".join(ret)
  
  
    
​
class Quarter(object):
  def __init__(self, name, result):
    self.name = name
    self.result = result
    
  def __lt__(self, other):
    return (self.result, other.name) < (other.result, self.name)
    
  def __repr__(self):
    if self.result == 0:
      return self.name+"|"+"#"*(self.result//50)+str(self.result)
    else:
      return self.name+"|"+"#"*(self.result//50)+" "+str(self.result)

