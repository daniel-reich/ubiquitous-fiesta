
def decode(txt):
  code={'a':16,'b':17,'c':18,'d':1,
        'e':2,'f':3,'g':4,'h':5,
        'i':6,'j':7,'k':8,'l':9,
        'm':10,'n':2,'o':3,'p':4,
        'q':5,'r':6,'s':7,'t':8,
        'u':9,'v':10,'w':11,'x':12,
        'y':4,'z':5,' ':5
  }
  result=list()
  for i in txt:
    if(i>='a' and i<='z'):  
      result.append(code[i.lower()])
    elif(i>='A' and i<='Z'):
      result.append(code[i.lower()]+4)
    elif(i==' '):
      result.append(5)
  return result

