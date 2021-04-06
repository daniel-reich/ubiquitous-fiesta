
def is_harshad(num):
  numstring = str(num)
  numsum = 0
  for i in range(0,len(numstring)):
    numsum += int(numstring[i])
  if numsum != 0:
    if num % numsum == 0:
        return True
    else:
        return False
  else:
    return False

