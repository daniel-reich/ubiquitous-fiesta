
def is_harshad(num):
  try:
    return num%sum(int(i) for i in str(num))==0
  except:
    return False

