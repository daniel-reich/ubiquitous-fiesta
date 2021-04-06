
def sequence_generator(seq):
  def ari(n):
    return seq[0] + com*(n-1)
  def geo(n):
    return seq[0]*(com**(n-1))
  
  if seq[2]-seq[1] == seq[1]-seq[0]:
    com = seq[1]-seq[0]
    return ari
  elif seq[2]/seq[1] == seq[1]/seq[0]:
    com = seq[1]/seq[0]
    return geo

