
def is_consecutive(s):
  def group_by_size(string, size):
    if len(string) == size:
      return [string]
    elif len(string) < size:
      return ['X']
    else:
      return [string[:size]] + group_by_size(string[size:], size)
  def consecutive(group, index = 0, previous = None, direct = None):
    if previous == None:
      previous = int(group[index])
      return consecutive(group, index+1, previous)
    else:
      if index == len(group):
        return True
      elif direct == None:
        if int(group[index]) not in [previous - 1, previous + 1]:
          return False
        elif int(group[index]) == (previous - 1):
          direct = 'd'
        else:
          direct = 'a'
        
        return consecutive(group, index+1, int(group[index]), direct)
      else:
        if direct == 'a':
          if int(group[index]) != previous + 1:
            return False
          else:
            return consecutive(group, index+1, int(group[index]), direct)
        else:
          if int(group[index]) != previous - 1:
            return False
          else:
            return consecutive(group, index+1, int(group[index]), direct)
  
  valid_groups = [group_by_size(s,n) for n in range(1, len(s) // 2 + 1) if 'X' not in group_by_size(s,n)]
  consecs = [consecutive(group) for group in valid_groups]
  print(s)
  return True in consecs

