
def full_key_name(piece):
  x = piece.split()
  if x[-1][0].isupper():
    return " ".join(x[:-1])+" "+x[-1].capitalize()+' '+"major"
  else:
    return " ".join(x[:-1])+" "+x[-1].capitalize()+' '+"minor"

