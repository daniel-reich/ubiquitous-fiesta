
def ascending(txt):
  for i in range(1, len(txt)):
    if len(txt)/i == float(len(txt)//i):
      passed = True
      for j in range(1, len(txt)//i):
        if not int(txt[i*j:i*(j+1)]) == int(txt[i*(j-1):i*j]) + 1:
          passed = False
          break
      if passed:
        return True
  return False

