
def worm_length(worm):
  res = [i for i in worm if i=="-"]
  return ("invalid" if not worm or len(res) != len(worm) 
          else str(len(res)*10) + " mm.")

