
def one_odd_one_even(n):
 k = str(n)
 s = [int(i) for i in k]
 if (s[0]%2==0 and s[1]%2 !=0) or ( s[0]%2!=0 and s[1]%2 ==0):
  return True
 else:
   return False

