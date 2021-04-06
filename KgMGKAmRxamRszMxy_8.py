
def spartans_cipher(message, n_Slide):
  if message:
    k=n_Slide-len(message)%n_Slide if len(message)%n_Slide else 0
    message=message+'*'*k
    t=len(message)//n_Slide
    A=[message[i:i+t] for i in range(0, len(message), t)]
    B=[''.join(x) for x in zip(*A)]
    return ''.join(B).replace('*', ' ').strip()
  else:
    return ''

