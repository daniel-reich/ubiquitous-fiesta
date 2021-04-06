
def encrypt(word):
  rev = word[::-1]
  new=""
  i=0
  while i<len(rev):
    if rev[i]=="a":
      new=new+"0"
    elif rev[i]=="e":
      new=new+"1"
    elif rev[i]=="o":
      new=new+"2"
    elif rev[i]=="u":
      new=new+"3"
    else:
      new=new+rev[i]
    i=i+1
  new=new+"aca"
  return new

