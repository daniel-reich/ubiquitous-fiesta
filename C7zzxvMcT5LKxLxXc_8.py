
def decode(txt):
    lst=[]
    for i in txt:
      val=ord(i)
      add=0
      while(val!=0):
        rem=val%10
        add=add+rem
        val=val//10
      lst.append(add)
    return lst

