
def increment_string(x):
  listX=list(x)
  kumangka=[]
  for i in listX:
    if i.isdigit():
      kumangka.append(i)
  for j in kumangka:
    del listX[listX.index(j)]
  if len(kumangka)==0:
    listX.append("1")
    return "".join(listX)
  elif len(kumangka)!=0:
      if kumangka[0]!="0":
        nilai=int("".join(kumangka))+1
        listX.append(str(nilai))
        return "".join(listX)
      elif kumangka[0]=="0":
        nol=[]
        i=0
        while kumangka[i]=="0":
          nol.append(kumangka[i])
          del kumangka[0]
        nilai=int("".join(kumangka))+1
        lis=list(str(nilai))
        if len(lis)>len(kumangka):
          del nol[-1]
          hasil=nol+lis
          hasil=listX+hasil
          print(hasil)
          return "".join(hasil)
        elif len(lis)==len(kumangka):
          listx=listX+nol+lis
          return "".join(listx)

