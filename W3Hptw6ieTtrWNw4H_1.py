
d ={'a':11,'b':12,'c':13,'d':14,'e':15,'f':21,'g':22,'h':23,'i':24,
        'j':24,'k':25,'l':31,'m':32,'n':33,'o':34,'p':35,'q':41,'r':42,
        's':43,'t':44,'u':45,'v':51,'w':52,'x':53,'y':54,'z':55}
def polybius(text):
  out= ''
  lst=[word for word in text.split()]
  if(lst[0][0].lower() in d.keys()):
    for word in lst:
      for c in word:
        if (c.isalpha()):
          out+=str(d[c.lower()])
      out+=' '
  else:
    for word in lst:
      for i in range (0,len(word),2):
        for k, v in d.items():
          if (v== int(word[i]+word[i+1])):
            if(v==24):
              if(k=='i'):
                out+=k
            else:
              out+=k
        out+=' '
  return out[:-1]
​
def bifid(text):
  a1,out=''.join(polybius(text).split()),''
  if len(a1)!= len(text)*2:
    a2 = ([(a1[k]) for k in range (len(a1)) if k%2==0],[(a1[k]) for k in range (len(a1)) if k%2==1])
    a3=(a2[0]+a2[1])
  else:
    a2 = ([(a1[k]) for k in range (len(a1)//2)],[(a1[k]) for k in range (len(a1)//2,len(a1))])
    a3=''
    for i in range (len(a2[0])):
      a3+=(a2[0][i]+a2[1][i])
  for i in range(0,len(a3),2):
    for k, v in d.items():
      if int(a3[i]+a3[i+1])==v:
        if (v==24):
          out+=('i')
          break
        else:
          out+=k
  return out

