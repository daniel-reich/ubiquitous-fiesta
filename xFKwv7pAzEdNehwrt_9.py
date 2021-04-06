
def bracket_logic(xp):
  dict_b = {'[':']','{':'}','(':')','<':'>'}
  lst = [i for i in xp if i in '()[]{}<>']
  unwanted = [1]
  while len(unwanted) > 0:
    unwanted = []
    for i in range(len(lst)):
      for j in dict_b:
        try:
          if lst[i] == j and lst[i+1] == dict_b[j]:
            unwanted.append(i)
            unwanted.append(i+1)
        except:
          continue
  
    for ele in sorted(unwanted, reverse = True):  
      del lst[ele]
  
  return len(lst) == 0

