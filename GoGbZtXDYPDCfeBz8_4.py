
def magic(txt):
    mm, dd, yy = txt.split()
    mmxdd = str(int(mm) * int(dd))
    if len(mmxdd) == 1 and mmxdd == yy[3]:  return True
    if len(mmxdd) == 2 and mmxdd == yy[2:]: return True
    if len(mmxdd) == 3 and mmxdd == yy[1:]: return True
    return False

