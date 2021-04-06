
def expanded_form(num):
  lst=[]
  for i,j in enumerate(str(num)):
    if j != "0":
      lst.append(str(int(j)* 10**(len(str(num))-i-1)))
  return " + ".join(lst)

