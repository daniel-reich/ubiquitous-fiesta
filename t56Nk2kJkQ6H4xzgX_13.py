
def swap_xy(txt):
  switch=False
  a="0123456789"
  f=""
  g=""
  val1=[]
  val2=[]
  for t in txt:
    if t==")":
      if switch==True:
        val2.append(f)
        f=""
      else:
        val1.append(f)
        f=""
      switch=True
    else:
      if t in a or t=="-":
        f=f+t
      else:
        if len(f)>0 and switch== False:
          val1.append(f)
          f=""
        elif len(f)>0 and switch==True:
          val2.append(f)
          f=""
  f="("+val1[1]+","+" "+val1[0]+")"+","+" "+"("+val2[1]+","+" "+val2[0]+")"
  return f

