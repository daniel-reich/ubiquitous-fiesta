
def group_seats(lst, n):
  f=0
  for i in lst:
    
    for c in range(len(i)):
      a=c
      count=0 
      if i[a]==0 : 
        while i[a]==0 :
          a=a+1
          if count<n: count=count+1
          if a==len(i): break
          
                    
                        
      if count==n: 
          f=f+1
          print(i)
            
      
  
  return f

