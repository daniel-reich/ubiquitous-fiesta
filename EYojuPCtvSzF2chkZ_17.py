
def get_filename(path):
  c=''
  for i in path:
    c=c+i
    if i=='/':
      c=''
  return c

