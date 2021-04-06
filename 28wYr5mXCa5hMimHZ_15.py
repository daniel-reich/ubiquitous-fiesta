
def valid_name(name):
  k = name.split(" ")
  if len(k) in (2,3) and '.' not in k[-1]:
    for i in k:
      if i[0].isupper():
        continue
      else:
        return False
        break
    else:
      if "." not in k[0] and '.' not in k[1] and len(k[0])!=1 and len(k[1])!=1:
        return True
      elif "." in k[1] and len(k[1])==2 and '.' not in k[0] and len(k[0])!=1:
        return True
      elif "." in k[0] and len(k[0])==2 and k[1]==k[-1]:
        return True
      elif "." in k[0] and '.' in k[1] and len(k[0])==2 and len(k[1])==2:
        return True 
      else:
        return False
  else:
    return False

