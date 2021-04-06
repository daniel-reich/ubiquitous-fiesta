
def create_square(l):
  if l is None or l<1:return''
  if l==1:return'#'
  else:return'\n'.join(['#'*l]+['#'+' '*(l-2)+'#'for i in range(l-2)]+['#'*l])

