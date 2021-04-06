
def magic(txt):
  return txt.split()[2].endswith(str(int(txt.split()[0]) * int(txt.split()[1])))

