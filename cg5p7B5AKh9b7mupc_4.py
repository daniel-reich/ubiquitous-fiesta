
def check_inclusion(s1, s2):
  def is_permutation(string, index, lst):
    try:
      if lst == []:
        return True
    
      elif string[index] not in lst:
        return False
    
      else:
        lst.pop(lst.index(string[index]))
        return is_permutation(string, index+1, lst)
    except IndexError:
      return False
  
  permutations = [is_permutation(s2, index, list(s1)) for index in range(len(s2))]
  return True in permutations

