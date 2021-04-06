
from math import ceil
def spartans_cipher(message, n_Slide):
  x = ceil(len(message)/n_Slide)
  if not message: return ""
  lst = [message[i:i+x] for i in range(0,len(message),x)]
  lst[-1] += (4-len(message)%4)%4*" "
  lst += [x*" "]*(n_Slide-len(lst))
  return ''.join(sum(zip(*lst),())).strip()

