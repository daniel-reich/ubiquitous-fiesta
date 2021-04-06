
def lambda_to_def(code):
  ret = 'def '
  ret+=code.split(' =')[0]
  ret+='('
  ret+=code.split('lambda ')[1].split(':')[0]
  ret+='):\n\treturn'
  ret+=':'.join(code.split(':')[1:])
  return ret

