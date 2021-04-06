
m=["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
def dance_convert(n):
  if any(not i.isnumeric() for i in str(n)) or len(n)<4: 
    return 'Invalid input.'
  return [m[(int(str(n)[i])+i)%10] for i in range(len(n))]

