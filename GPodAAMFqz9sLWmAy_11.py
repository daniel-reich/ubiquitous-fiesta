
def one_odd_one_even(n):
  n= str(n)
  if int(n[0]) % 2 == 0 and int(n[1]) %2 !=0:
    return(True)
  if int(n[1]) %2 == 0 and int(n[0]) %2 != 0:
    return (True)
  else:
    return(False)

