
def closest_palindrome(num):
  n=0
  while num:
    if str(num-n)==str(num-n)[::-1]:
      return num-n
    elif str(num+n)==str(num+n)[::-1]:
      return num+n
    n+=1

