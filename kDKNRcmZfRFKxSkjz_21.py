
def unmix(txt):
  return "".join(txt[i:i+2][::-1] for i in range(0,len(txt),2))

