
def quad_sequence(lst):
  length = len(lst)
  n = (lst[2]-lst[1])-(lst[1]-lst[0])
  while len(lst)<length*2:
    diff = lst[-1]-lst[-2]
    diff+=n
    lst.append(lst[-1]+diff)
  return lst[len(lst)//2:]

