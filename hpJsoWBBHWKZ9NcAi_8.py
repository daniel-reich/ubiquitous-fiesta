
def bird_code(lst):
  retVal = []
  for bird in lst:
    retVal.append(chk(bird))
  return retVal
​
​
def chk(a):
    a = a.replace("-", " ")
    split = a.split()
    length = len(split)
​
    retval = ""
    if length == 1:
        retval = a[:4]
    elif length == 2:
        retval = split[0][:2] + split[1][:2]
    elif length == 3:
        retval = split[0][:1] + split[1][:1] + split[2][:2]
    elif length == 4:
        retval = split[0][:1] + split[1][:1] + split[2][:1] + split[3][:1]
​
    return retval.upper()

