
def get_case(txt):
  sCase=""
  tmpCase=""
  cnt=0
  a=len(txt)
  for i in range(0,a):
    if(txt[i].isalpha()):
      if(txt[i].islower()):
        sCase="lower"
      else:
        sCase="upper"
      if(cnt>0):
        if(tmpCase!=sCase):
          return "mixed"
      cnt=cnt+1
      tmpCase=sCase
  return sCase

