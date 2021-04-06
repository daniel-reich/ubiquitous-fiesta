
def bowling(pins):
  f,i = [],0
  while len(f) < 10:
      if pins[i]==10:
          f.append(sum(pins[i:i+3]))
          i+=1
      elif sum(pins[i:i+2])==10:
          f.append(sum(pins[i:i+3]))
          i+=2
      else:
          f.append(sum(pins[i:i+2]))
          i+=2
  return sum(f)

