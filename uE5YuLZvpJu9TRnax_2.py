
def prefix(exp):
  items = exp.replace('/','//').split(' ')
  i = len(items)-1
  while i>=0:
    if items[i] in '*+-//':
      items[i:i+3] = [str(eval("({}){}({})".format(items[i+1],items[i],items[i+2])))]
    i-=1
  return int(items[0])

