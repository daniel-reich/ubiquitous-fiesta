
def convert_binary(string):
  atom ='abcdefghijklmABCDEFGHIJKLM'
  ans = []
  for x in string:
    if x in atom:
      ans.append('0')
    else:
      ans.append('1')
  return ''.join(ans)

