
def society_name(friends):
  code = ''
  friends = sorted(friends)
  for name in friends:
    code += name[0]
  code = code.upper()
  return code

