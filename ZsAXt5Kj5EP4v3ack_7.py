
def secret(txt):
  txt = txt.split('>')
  final = '<{}>'.format(txt[0])
  tag = "<{0} class='{1}$'></{0}>".format(txt[1].split('.')[0],txt[1].split('.')[1].split('$')[0])
  tag = tag.replace('$','{}')
  for i in range(1,int(txt[1][-1])+1):
    final+=tag.format('0'*(txt[1].count('$')-1)+str(i))
  return final+'</{}>'.format(txt[0])

