
def is_exact(n,new_n=0,number=1):
  # Your recursive implementation of the code.
  if new_n==0:
    new_n=n
  if new_n==number or n==0:
    return [n,number]
  if new_n%number==0:
    new_n=new_n//number
    return is_exact(n,new_n,number+1)
  else:
    return 'Not exact!'

