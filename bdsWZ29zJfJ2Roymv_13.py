
def swap_two(txt):
  return "".join(txt[i+2:i+4]+txt[i:i+2] if i+4<=len(txt) else txt[i:] \
      for i in range(0,len(txt)+1,4))

