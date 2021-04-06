
def create_square(l):
  if l == 1 : return '#'
  return '' if not l or l<1 else '#'*l+('\n#'+' '* (l-2)+'#')*(l-2)+'\n'+'#'*l

