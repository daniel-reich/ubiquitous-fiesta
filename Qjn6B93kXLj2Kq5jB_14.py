
def simplify_frac(f):
  [a,b]=list(map(int,f.split("/")))
  def moq(a,b):
    return a  if b==0 else moq(b,a%b)
  
  return "{}/{}".format(a//moq(a,b),b//moq(a,b))

