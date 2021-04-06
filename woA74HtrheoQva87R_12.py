
def concat(*args):
    z =''
    for num in args:
      for i in range(0,len(num)):
       z= z+str(num[i])
    return list(float(num) if num.isalpha()==False  else num for num in z  )

