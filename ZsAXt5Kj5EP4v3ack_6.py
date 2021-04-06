
import re
def secret(txt):
  g = re.match(r'^(\w+)\>(\w+)\.(\w+)',txt)
  num = int(re.findall(r'\d+$',txt)[0])
  string = lambda x: '<{} class=\'{}\'></{}>'.format(g.group(2),g.group(3)+(txt.count('$')-1)*'0'+str(x),g.group(2))
  return '<{}>{}</{}>'.format(g.group(1),''.join(string(x) for x in range(1,num+1)),g.group(1))

