
def num_to_eng(n):
  z={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',
12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred'}
  if(n in z.keys()):
    return z[n]
  else:
    x=1
    ans=''
    nn=n
    while(n>0):
      if(x==1):
        if(n%10!=0):
          ans+=z[n%10]+' '
        x+=1
      elif(x==2):
        x+=1
        if((n%10)!=0 and (n%10)!=1):
          ans=z[(n%10)*10]+' '+ans+' '
        elif((n%10)==1):
          ans=z[(nn%10)+10]+' '
      else: 
        ans=z[n%10]+' '+z[100]+' '+ans+' '
        x+=1
      n=n//10 
    return ans.rstrip()

