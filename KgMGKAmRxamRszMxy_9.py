
def spartans_cipher(message, n_Slide):
  n=len(message)//n_Slide
  if (len(message)%n_Slide)!=0:
    n+=1
  s=''
  for i in range(n):
    for j in range(n_Slide):
      if j*n+i<len(message):
        s+=message[j*n+i]
      elif (j*n+i)<(n*(n_Slide)):
        s+=" "
  return s.rstrip()

