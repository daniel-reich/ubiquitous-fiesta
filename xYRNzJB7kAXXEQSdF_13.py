
def wiggle_string(s):
  asc = [" "*i + s for i in range(0,len(s))] 
  desc = [" "*i + s for i in range(len(s),-1,-1)]
  return asc + desc

