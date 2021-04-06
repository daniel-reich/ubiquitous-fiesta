
def ini(name):
  pos = name.find(' ')
  return name[0] + '. ' + name[pos+1] + '.' 
​
def initialize(names):
  return [ini(name) for name in names]

