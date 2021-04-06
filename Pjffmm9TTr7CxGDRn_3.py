
def is_ascending(s):
  def group_by_size(string, size):
    if len(string) == size:
      return [string]
    elif len(string) < size:
      return ['XX']
    else:
      return [string[:size]] + group_by_size(string[size:], size)
  def ascending(group, index = 0, previous = None):
    if previous == None:
      previous = int(group[index])
      return ascending(group, index+1, previous)
    else:
      if index == len(group):
        return True
      elif int(group[index]) != previous + 1:
        return False
      else:
        return ascending(group, index + 1, int(group[index]))
      
  poss_groups = [group_by_size(s,n) for n in range(1, len(s) // 2 + 1) if 'XX' not in group_by_size(s,n)]
  asc = [ascending(group) for group in poss_groups]
  
  return True in asc

