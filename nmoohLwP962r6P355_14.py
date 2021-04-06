
def straight_digital(number):
  lst=str(number)
  c=0
  if number<100:
    return "Not Straight"
  elif len(set(lst))==1:
    return "Trivial Straight"
  else:
    for i in range(len(lst)-1):
      s=int(lst[1])-int(lst[0])
      if int(lst[i+1])-int(lst[i])==s:
        c=c+1
    if c==(len(lst)-1):
      return s
    else:
      return "Not Straight"

