
def create_square(length):
  if not isinstance(length,int) or length<1:
    return ''
  ret = ''
  if length>1:
    ret+=('#'*length)+'\n'
  for i in range(2,length):
    ret+='#'+(' '*(length-2))+'#\n'
  if length>0:
    ret+='#'*length
  return ret

