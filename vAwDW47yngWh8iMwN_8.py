
def cap_last(txt):
  return "".join(txt[i].upper() if txt[i+1]==" " else txt[i] for i in range(len(txt)-1))+txt[-1].upper()

