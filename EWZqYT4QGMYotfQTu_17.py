
import re
table = (('a','b','c','d','e'),('f','g','h','i','j'),('l','m','n','o','p'),('q','r','s','t','u'),('v','w','x','y','z'))
def tap_code(text):
  global table
  if '.' in text:
    lst = [(len(i.split()[0])-1,len(i.split()[1])-1) for i in re.findall("[^\ ]+\ [^\ ]+", text)]
    return ''.join(table[i[0]][i[1]] for i in lst)
  else:
    text = text.replace('k','c')
    lst = [find(i) for i in text]
    return ' '.join('.'*j for i in lst for j in i)
​
def find(c):
  global table
  for ndx, row in enumerate(table):
    if c in row:
      return (ndx+1,row.index(c)+1)

