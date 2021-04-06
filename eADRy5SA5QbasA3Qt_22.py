
def is_harshad(n):
 str1=str(n)
 listharshad=list(str1)
​
 listharshad=[int(i) for i in listharshad]
 print(listharshad)
 sum1=(sum(listharshad))
 if n % sum1 ==0:
   return(True)
 else:
   return(False)

