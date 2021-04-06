
def switches(n):
  if n==1 or n==2:
    return n
  start,counter,end_switch, pos,num,j =[0 if i <n-1 else 1 for i in range(n)],1,1,n-1,n,0
  while j < num//2:
    while not (start[0]==1 and start[1]==1):
      for i in range (n-2,-1,-1):
        if end_switch == 1 and pos !=i:
          if(start[i]==0) and sum(start[i+1:])==1 and start[i+1]==1:
            start[i],pos=1,i
            counter+=1
            break
          if (start[i]==1) and sum(start[i+1:])==1 and start[i+1]==1:
            start[i],pos=0,i
            counter+=1
            break
          end_switch,pos=0,n-1
          start[n-1]=end_switch
          counter+=1
          break
        
        elif end_switch==0 and pos !=i:
          if (start[i]==1):
            if (sum(start[i+1:])==1 and start[i+1]==1):
              start[i],pos=0,i
              counter+=1
              break
          else:
            if (sum(start[i+1:])==1 and start[i+1]==1):
              start[i],pos=1,i
              counter+=1
              break
            else:
              if (i==0):
                end_switch,pos,=1,n-1
                start[n-1]=end_switch
                counter+=1
                break
    j+=1
    n=n-2
    if (n>2):
      start,pos,end_switch =[0 if i <n-1 else 1 for i in range(n)],n-1,1
      counter+=1
    elif n==1:
      return (counter+1)
    else:
      return (counter+2)

