
def createPolybiusSquare(keyword):
  k, keyword_ended,kk,psq,counter=0,False,0,[['' for i in range(5)] for j in range(5)],0
  for i in range (5):
    j=0
    while j<5:
      if k<len(keyword):
        psq[i][j]=keyword[k].upper()
        k+=1
        j+=1
      else:
        if not (chr(65+kk) in keyword.upper() or chr(65+kk)=='J'):
          psq[i][j]=chr(65+kk)
          kk+=1
          j+=1
        else:
          kk+=1
  return psq
  
def bigramsCreation(txt):
  i=extra=0
  bigrams,letters ='',''
  while i< len(txt)-1:
    if txt[i]==txt[i+1]:
      bigrams+=txt[i]+'x'+ ' ' + txt[i+1]
      letters+=txt[i]+txt[i+1]
      extra=1
      i+=2
    else:
      if extra==1:
        bigrams+=txt[i]+ ' '
        letters+=txt[i]
        extra=0
        i+=1
      else:
        bigrams+=txt[i]+txt[i+1]+' '
        letters+=txt[i]+txt[i+1]
        i+=2
        
  if len(letters) < len (txt):
    bigrams+=txt[-1]+'x'
  return bigrams
​
​
def playfair(txt, keyword):
  keyword1=''
  for c in keyword:
    if not c in keyword1:
      keyword1+=c
  psq= createPolybiusSquare(keyword1)
  if (txt.split()[0]==txt):
    cipher=False
  else:
    cipher=True
  txt1,out= ''.join([c[i].lower() for c in txt.split() for i in range (len(c)) if c[i].isalpha()]),''
  bigrams = bigramsCreation(txt1)
  for bi in bigrams.split():
    col_or_row=False
    for i in psq:
      if bi[0].upper() in i and bi[1].upper() in i:
        col_or_row=True
        if (cipher):
          for k in range (2):
            if i.index(bi[k].upper())+1 <=4:
              out+= i[i.index(bi[k].upper())+1]
            else:
              out+= i[(i.index(bi[k].upper())+1)%5]
        else:
          for k in range (2):
            if i.index(bi[k].upper())-1 >=0:
              out+= i[i.index(bi[k].upper())-1]
            else:
              out+= i[4]
​
    for j in range(5):
      if (col_or_row):
        break
      col=[]
      for i in psq:
        col.append(i[j])
      if bi[0].upper() in col and bi[1].upper() in col:
        col_or_row=True
        for k in range (2):
          if cipher:
            if col.index(bi[k].upper())+1 <=4:
              out+= col[col.index(bi[k].upper())+1]
            else:
              out+= col[(col.index(bi[k].upper())+1)%5]
          else:
            if col.index(bi[k].upper())-1 >=0:
              out+= col[col.index(bi[k].upper())-1]
            else:
              out+= col[4]
​
    if not (col_or_row):
      for i in range (5):
        for j in range (5):
          if bi[0].upper() == psq[i][j]:
            one=(i,j)
          if bi[1].upper() == psq[i][j]:
            two=(i,j)
      out+=psq[one[0]][two[1]]
      out+=psq[two[0]][one[1]]
  
  return out

