
def full_key_name(piece):
  n = piece.rfind('in ')
  if n < 0:
    return piece
  c = piece[n+3]
​
  if c.islower():
    ret = c.upper()
    end = ' minor'
  else:
    ret = c
    end = ' major'
  if (n+3) == len(piece)-1:
    return piece[:n+3]+ret + end
  else:
    return piece[:n+3]+ret+piece[-1]+end

