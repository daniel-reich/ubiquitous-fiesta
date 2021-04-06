
def break_point(num):
    lnum = [i for i in str(num)]
    for i in range(len(lnum)):
      caca1 = (lnum[:i])
      caca2 = (lnum[i:])
      teta1 = 0
      teta2 = 0
      for i in caca1:
        teta1 += int(i)
      for i in caca2:
        teta2 += int(i)
      if caca1 != "":
        if teta1 - teta2 == 0:
          return True
          break
    return False

