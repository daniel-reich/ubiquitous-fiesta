
def same_upsidedown(ntxt):
  return "".join(["6" if i=="9" else "9" if i=="6" else "0" for i in str(ntxt)][::-1])==str(ntxt)

