
def divisible_by_left(n):
   ans=[False,]
   n=str(n)
   for i in range(1,len(n)):
       try:
           if int(n[i])%int(n[i-1])==0:
              ans.append(True)
           else:
              ans.append(False)
       except ZeroDivisionError:
           ans.append(False)
           
   return ans

