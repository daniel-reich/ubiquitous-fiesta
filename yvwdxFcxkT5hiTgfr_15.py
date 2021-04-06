
def get_xp(d):
  #return str(sum(val*5*2**index for index, val in enumerate(d)))+'XP'
  
  keys = ['Very Easy','Easy', 'Medium', 'Hard', 'Very Hard']
  return str(sum(d[keys[index]]*5*2**index for index in range(len(keys))))+'XP'

