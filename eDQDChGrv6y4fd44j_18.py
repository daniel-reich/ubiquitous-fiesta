
def can_put(txt,dim):
  spl = txt.split()
  if(len(txt) <= dim[1]):
    return True
  elif(len(spl) <= dim[0]):
    kl = 0
    result = True
    while(kl < len(spl)):
      if(len(spl[kl]) > dim[1]):
        result = False
        break
      kl += 1
    return result
  else:
    return False

