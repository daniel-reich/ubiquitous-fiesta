
def closest_palindrome(num):
  anum = num
  while str(anum) != str(anum)[::-1]:
    anum+=1
  upperlimit=anum
  anum = num
  while str(anum) != str(anum)[::-1]:
    anum-=1
  lowerlimit=anum
  if upperlimit-num < num-lowerlimit:
    return upperlimit
  else:
    return lowerlimit

