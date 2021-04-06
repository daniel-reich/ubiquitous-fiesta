
def flatten(r):
  # Your recursive solution here.
  return eval('['+str(r).replace('[','').replace(']', '')+']')

