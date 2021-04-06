
def difference_by_one(words):
  def difference():
    return abs(len(words[0]) - len(words[1]))
  if difference() > 1:
    return False
  elif difference() == 1:
    words.sort(key = lambda x: len(x))
    if words[0]== words[1][:-1]:
      return True
    elif words[0] == words[1][1::]:
      return True
    else:
      for i in range(0,len(words[1])):
        if words[0][i] != words[1][i]:
          return words[0] == words[1][:i] + words[1][i+1::]         
  else:
    diff = 0
    for i in range(0,len(words[0])):
      if words[0][i] != words[1][i]:
        if diff == 0:
          diff += 1
        else:
          return False
    return True
        
      
def isWordChain(words):
  for i in range(0,len(words)-1):
    if difference_by_one([words[i],words[i+1]]) == False:
      return False
  return True

