
def salt(t):
  salt=10
  saltout=0
  for n in range (t*600):
    salt= salt+0.1/600-10/600*salt/100
  return(round(salt,3))

