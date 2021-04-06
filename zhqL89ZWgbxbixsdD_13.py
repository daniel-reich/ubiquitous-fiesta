
def fn(n,count,z):
  if n%1!=0:
    return "Not exact!"
  elif n==1:
    return [z,count-1]
  else:
    n=n/count
    count=count+1
    return fn(n,count,z)
def is_exact(n):
  # Your recursive implementation of the code.
  return fn(n,1,n)

