
def magic(txt):
  a=txt.split()
  return True if int(a[0])*int(a[1])==int(a[2][-len(str(int(a[0])*int(a[1]))):]) else False

