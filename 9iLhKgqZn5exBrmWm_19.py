
def ascending(txt):
  i = 1
  while i < len(txt):
    if not len(txt)%i:
      temp = [int(txt[j:j+i]) for j in range(0,len(txt),i)]
      if all(temp[k] == temp[k-1]+1 for k in range(1,len(temp))):
        return True
    i += 1
  return False

