
def neighboring(txt):
  return all(ord(txt[i])+1 == ord(txt[i+1]) 
        or ord(txt[i])-1 == ord(txt[i+1]) 
        for i in range(len(txt)-1))

