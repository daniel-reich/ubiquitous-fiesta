
def spartans_cipher(message, n_Slide):
  while len(message)%n_Slide!=0:
    message+=" "
  n = len(message)//n_Slide
  cols = {i:'' for i in range(n)}
  for i in range(len(message)):
    cols[i%n]+=message[i]
  return ''.join(cols[i] for i in range(n)).strip()

