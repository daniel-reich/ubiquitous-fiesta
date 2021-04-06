
def same_upsidedown(ntxt):
  return ntxt[::-1] == "".join(i if i not in "69" else "9" if i=="6" else "6" for i in ntxt)

