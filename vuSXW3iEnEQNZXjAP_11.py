
def create_square(length):
  if length:
    return '#'*length+('\n#'+' '*(length-2)+'#')*(length-2)+('\n'+'#'*length)*(length>1)
  else: return ''

