
def kaprekar(num):
  final=[]
  if(num==6174):
    return 0
  def kaprekar1(num):
    y=str(num)
    init=[]
    for x in range(len(y)):
      init.append(int(y[x:x+1]))
    first=sorted(init, reverse=True)
    last=sorted(init)
    fff=""
    lll=""
    for x in first:
      fff+=str(x)
    for i in last:
      lll+=str(i)
    end=int(fff)-int(lll)
    if(len(str(end))==3):
      end=end*10
    if(end!=6174):
      kaprekar1(end)
      final.append(1)
    else:
      return final
  kaprekar1(num)
  return(len(final)+1)

