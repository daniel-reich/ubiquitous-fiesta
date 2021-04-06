
def closest_palindrome(n):
 a=n
 while str(a)!=str(a)[::-1]:a-=1
 b=n
 while str(b)!=str(b)[::-1]:b+=1
 return min(a,b,key=lambda x:abs(n-x))

