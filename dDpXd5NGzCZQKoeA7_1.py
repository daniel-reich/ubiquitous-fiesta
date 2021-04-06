
def num_args(func, n=0):
  try: eval('func(%s)' % ('1,'*n)); return n
  except: return num_args(func, n+1)

