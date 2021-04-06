
def is_harshad(n):
  templist = [int(number) for number in str(n)]
  if n % sum(templist) == 0:
      return True
  else:
      return False

